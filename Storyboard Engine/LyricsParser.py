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
    def __init__(self, fontPath="C:/Windows/Fonts/A-OTF-GothicBBBPr5-Medium.otf", fontSize=60, filePath="SB/lyrics"):
        self.characters = []
        self.width = []
        self.fontPath = fontPath
        self.fontSize = fontSize
        self.filePath = filePath
        pygame.init()
        self.font = pygame.font.Font(self.fontPath, self.fontSize)
        isExists = os.path.exists(self.filePath)
        if not isExists:
            os.makedirs(self.filePath)

    def setCh(self, letter):
        if letter.character not in self.characters:
            self.characters.append(letter.character)
            self.chRender(len(self.characters)-1)
            letter.width = self.width[len(self.characters)-1]
            letter.filename = self.IDtoFilename(len(self.characters)-1)
        letter.id = self.characters.index(letter.character)
        letter.width = self.width[len(self.characters) - 1]
        letter.filename = self.IDtoFilename(len(self.characters) - 1)
        return

    def IDtoFilename(self, id):
        if id % 10 == 0:
            name = self.filePath + str(int(id/10)) + 'x.png'
        else:
            name = self.filePath + str(id) + '.png'
        return '"'+name+'"'

    def chRender(self, index):
        character = self.characters[index]
        rtext = self.font.render(character, True, (255, 255, 255))
        if self.characters.index(character)%10 == 0:
            name = str(int(self.characters.index(character)/10))+'x'
        else:
            name = str(self.characters.index(character))
        self.width.append(rtext.get_size()[0])
        pygame.image.save(rtext, os.path.join(self.filePath, name+".png"))

class Sentence():
    def __init__(self, s='', t1=0, t2=0, CharacterRenderer=None):
        self.letters = []
        self.s = s
        self.start_t = t1
        self.end_t = t2
        if s != '':
            for ch in s:
                letter = Letter(ch, 0, t1, t2)
                CharacterRenderer.setCh(letter)
                self.letters.append(letter)

    def settime(self, t1, t2):
        self.start_t = t1
        self.end_t = t2

    def append(self, letter):
        self.letters.append(letter)


class LyricParser():
    def __init__(self, CharacterRenderer):
        self.sentences = []
        self.CR = CharacterRenderer

    def timingParser(self, time):
        elements = time.split(':')
        h = int(elements[0])
        m = int(elements[1])
        s = float(elements[2])
        ms = int(((h*60 + m) * 60 + s) * 1000)
        return ms

    def AssReader(self, filename):
        if '.ass' not in filename:
            raise RuntimeError("Incorrect ass file!")
        file = open(filename, encoding='utf8', errors='ignore')
        for line in file:
            if 'Dialogue:' in line:
                if '{\\k' not in line:
                    continue
                args = line.split(',')
                t1 = self.timingParser(args[1])
                t2 = self.timingParser(args[2])
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
                        self.CR.setCh(letter)
                        currentS.append(letter)
                        currentS.s += ch
                    currentT = currentT2
                self.sentences.append(currentS)

    def get_sentences(self):
        return self.sentences

    def ParseTest(self):
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
    LP.AssReader(os.path.join('H:\python-workspace\oriental blossom','subtitles.ass'))
    sentences = LP.get_sentences()
    sentences.append(Sentence('麻花牛逼', 500, 1000, CR))
    for sen in sentences:
        print(sen.s, sen.start_t, sen.end_t)
