# coding: utf-8
import os
import pygame
from tools.utils import *


class Letter:
    def __init__(self, ch, i, t1, t2):
        self.character = ch
        self.id = i
        self.start_t = t1
        self.end_t = t2
        self.width = 0
        self.filename = ''


# fontPath e.g.: os.path.join("C:/Windows/Fonts", "A-OTF-GothicBBBPr5-Medium.otf")
# fontSize e.g.: 60
# filePath e.g.: SB/lyrics
class CharacterRenderer:
    def __init__(self, font_path="C:/Windows/Fonts/A-OTF-GothicBBBPr5-Medium.otf", font_size=60, file_path="SB/lyrics"):
        self.characters = []
        self.width = []
        self.font_path = font_path
        self.font_size = font_size
        self.file_path = file_path
        pygame.init()
        self.font = pygame.font.Font(self.font_path, self.font_size)

    def set_ch(self, letter):
        if letter.character not in self.characters:
            self.characters.append(letter.character)
            #self.ch_render(len(self.characters)-1)
            self.width.append(self.font.size(letter.character)[0])
            letter.width = self.width[len(self.characters)-1]
            letter.filename = self.id_to_filename(len(self.characters)-1)
            letter.index = len(self.characters)-1
        else:
            letter.id = self.characters.index(letter.character)
            letter.width = self.width[letter.id]
            letter.filename = self.id_to_filename(letter.id)
        return

    def id_to_filename(self, id):
        if id % 10 == 0:
            name = self.file_path + str(int(id/10)) + 'x.png'
        else:
            name = self.file_path + str(id) + '.png'
        return '"'+name+'"'

    def render(self):
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path)
        for i in range(len(self.characters)):
            self.ch_render(i)

    def ch_render(self, index):
        character = self.characters[index]
        r_text = self.font.render(character, True, (255, 255, 255))
        if self.characters.index(character)%10 == 0:
            name = str(int(self.characters.index(character)/10))+'x'
        else:
            name = str(self.characters.index(character))
        self.width.append(r_text.get_size()[0])
        pygame.image.save(r_text, os.path.join(self.file_path, name+".png"))


class Sentence:
    def __init__(self, content='', start_t=normalize_timing_format(0), end_t=normalize_timing_format(0),
                 character_renderer=None):
        self.letters = []
        self.content = content
        self.start_t = normalize_timing_format(start_t)
        self.end_t = normalize_timing_format(end_t)
        if content != '':
            for ch in content:
                letter = Letter(ch, 0, start_t, end_t)
                character_renderer.set_ch(letter)
                letter.start_t = self.start_t
                letter.end_t = self.end_t
                self.letters.append(letter)

    def set_time(self, start_t, end_t):
        self.start_t = start_t
        self.end_t = end_t

    def append(self, letter):
        self.letters.append(letter)


class LyricParser:
    def __init__(self, character_renderer):
        self.sentences = []
        self.CR = character_renderer

    @staticmethod
    def timing_parser(time):
        elements = time.split(':')
        h = int(elements[0])
        m = int(elements[1])
        s = float(elements[2])
        ms = int(((h*60 + m) * 60 + s) * 1000)
        return ms

    def ass_reader(self, filename):
        if '.ass' not in filename:
            raise RuntimeError("Incorrect ass file!")
        file = open(filename, encoding='utf8', errors='ignore')
        for line in file:
            if 'Dialogue:' in line:
                args = line.split(',')
                if '{\\k' not in line:
                    t1 = self.timing_parser(args[1])
                    t2 = self.timing_parser(args[2])
                    self.sentences.append(Sentence(args[9][:-1], t1, t2, self.CR))
                    continue
                t1 = self.timing_parser(args[1])
                t2 = self.timing_parser(args[2])
                current_s = Sentence('', t1, t2)
                characters = args[9].split('{\\k')
                current_t = t1
                for character in characters:
                    if character == '':
                        continue
                    args2 = character.split('}')
                    current_t2 = current_t + int(args2[0]) * 10
                    for ch in args2[1]:
                        if ch == '\n':
                            continue
                        letter = Letter(ch, 0, current_t, current_t2)
                        self.CR.set_ch(letter)
                        current_s.append(letter)
                        current_s.content += ch
                    current_t = current_t2
                self.sentences.append(current_s)

    def get_sentences(self):
        return self.sentences

    def parse_test(self):
        i = 0
        for sentence in self.sentences:
            i += 1
            print(i, sentence.s, sentence.start_t, sentence.end_t)
            for letter in sentence.letters:
                print(' ', letter.character, letter.start_t, letter.end_t, letter.id, letter.width)


if __name__ == '__main__':
    # Create a characterRenderer first
    # Then create lyricParser, or directly add sentences
    CR = CharacterRenderer(font_path='Fonts/LEVIBRUSH.TTF', file_path='SB/letters/')
    LP = LyricParser(CR)
    LP.ass_reader('Subtitles\hana ni natta.ass')
    sentences = LP.get_sentences()
    #sentences.append(Sentence('麻花牛逼', 500, 1000, CR))
    #sentences.append(Sentence('yf大师牛逼', '00:50:123', '01:12:123', CR))
    for sen in sentences:
        print(sen.content, sen.start_t, sen.end_t)
        for ch in sen.letters:
            print(' ', ch.character, ch.width, ch.start_t, ch.end_t)
    #CR.render()