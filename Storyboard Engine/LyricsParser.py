# coding: utf-8
import os,shutil
import pygame


class Letter():
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
class CharacterRenderer():
    def __init__(self, font_path="C:/Windows/Fonts/A-OTF-GothicBBBPr5-Medium.otf", font_size=60, file_path="SB/lyrics"):
        self.characters = []
        self.width = []
        self.font_path = font_path
        self.font_size = font_size
        self.file_path = file_path
        pygame.init()
        self.font = pygame.font.Font(self.font_path, self.font_size)
        isExists = os.path.exists(self.file_path)
        if not isExists:
            os.makedirs(self.file_path)

    def set_ch(self, letter):
        if letter.character not in self.characters:
            self.characters.append(letter.character)
            self.ch_render(len(self.characters)-1)
            letter.width = self.width[len(self.characters)-1]
            letter.filename = self.id_to_filename(len(self.characters)-1)
        letter.id = self.characters.index(letter.character)
        letter.width = self.width[len(self.characters) - 1]
        letter.filename = self.id_to_filename(len(self.characters) - 1)
        return

    def id_to_filename(self, id):
        if id % 10 == 0:
            name = self.file_path + str(int(id/10)) + 'x.png'
        else:
            name = self.file_path + str(id) + '.png'
        return '"'+name+'"'

    def ch_render(self, index):
        character = self.characters[index]
        rtext = self.font.render(character, True, (255, 255, 255))
        if self.characters.index(character)%10 == 0:
            name = str(int(self.characters.index(character)/10))+'x'
        else:
            name = str(self.characters.index(character))
        self.width.append(rtext.get_size()[0])
        pygame.image.save(rtext, os.path.join(self.file_path, name+".png"))

class Sentence():
    def __init__(self, s='', t1=0, t2=0, character_renderer=None):
        self.letters = []
        self.s = s
        self.start_t = t1
        self.end_t = t2
        if s != '':
            for ch in s:
                letter = Letter(ch, 0, t1, t2)
                character_renderer.set_ch(letter)
                self.letters.append(letter)

    def settime(self, t1, t2):
        self.start_t = t1
        self.end_t = t2

    def append(self, letter):
        self.letters.append(letter)


class LyricParser():
    def __init__(self, character_renderer):
        self.sentences = []
        self.CR = character_renderer

    def timing_parser(self, time):
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
                if '{\\k' not in line:
                    continue
                args = line.split(',')
                t1 = self.timing_parser(args[1])
                t2 = self.timing_parser(args[2])
                currentS = Sentence('', t1, t2)
                characters = args[9].split('{\\k')
                currentT = t1
                for character in characters:
                    if character == '':
                        continue
                    args2 = character.split('}')
                    currentT2 = currentT + int(args2[0]) * 10
                    for ch in args2[1]:
                        if ch == '\n':
                            continue
                        letter = Letter(ch, 0, currentT, currentT2)
                        self.CR.set_ch(letter)
                        currentS.append(letter)
                        currentS.s += ch
                    currentT = currentT2
                self.sentences.append(currentS)

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
    CR = CharacterRenderer()
    LP = LyricParser(CR)
    LP.ass_reader(os.path.join('H:\python-workspace\oriental blossom','subtitles.ass'))
    sentences = LP.get_sentences()
    sentences.append(Sentence('麻花牛逼', 500, 1000, CR))
    for sen in sentences:
        print(sen.s, sen.start_t, sen.end_t)
