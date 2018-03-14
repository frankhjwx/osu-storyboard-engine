# coding: utf-8
import os,shutil
import pygame

class Letter():
    def __init__(self):
        self.character = ''
        self.id = 0
        self.start_t = 0
        self.end_t = 0
        self.width = 0
        self.filename = ''

    def __init__(self, ch, i, t1, t2):
        self.character = ch
        self.id = i
        self.start_t = t1
        self.end_t = t2
        self.width = 0
        self.filename = ''

    def set(self, ch, i, t1, t2):
        self.character = ch
        self.id = i
        self.start_t = t1
        self.end_t = t2


class CharacterRender():
    def __init__(self):
        self.characters = []
        self.width = []

    def setCh(self, letter):
        if letter.character not in self.characters:
            self.characters.append(letter.character)
        letter.id = self.characters.index(letter.character)
        return

    def IDtoFilename(self, id):
        if id % 10 == 0:
            name = 'SB/lyrics/' + str(int(id/10)) + 'x.png'
        else:
            name = 'SB/lyrics/' + str(id) + '.png'
        return '"'+name+'"'

    def chRender(self):
        pygame.init()
        font = pygame.font.Font(os.path.join("C:/Windows/Fonts", "A-OTF-GothicBBBPr5-Medium.otf"), 60)
        for character in self.characters:
            rtext = font.render(character, True, (255, 255, 255))
            if self.characters.index(character)%10 == 0:
                name = str(int(self.characters.index(character)/10))+'x'
            else:
                name = str(self.characters.index(character))
            self.width.append(rtext.get_size()[0])
            pygame.image.save(rtext, "test/"+name+".png")

class Sentence():
    def __init__(self):
        self.letters = []
        self.s = ''
        self.start_t = 0
        self.end_t = 0

    def __init__(self, t1, t2):
        self.letters = []
        self.s = ''
        self.start_t = t1
        self.end_t = t2

    def settime(self, t1, t2):
        self.start_t = t1
        self.end_t = t2

    def append(self, letter):
        self.letters.append(letter)


class LP():
    def __init__(self):
        self.sentences = []

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
        CR = CharacterRender()
        for line in file:
            if 'Dialogue:' in line:
                if '{\\k' not in line:
                    continue
                args = line.split(',')
                t1 = self.timingParser(args[1])
                t2 = self.timingParser(args[2])
                currentS = Sentence(t1, t2)
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
                        CR.setCh(letter)
                        currentS.append(letter)
                        currentS.s += ch
                    currentT = currentT2
                self.sentences.append(currentS)
        CR.chRender()
        for sentence in self.sentences:
            for letter in sentence.letters:
                letter.width = CR.width[letter.id]
                letter.filename = CR.IDtoFilename(letter.id)

    def ParseTest(self):
        i = 0
        for sentence in self.sentences:
            i += 1
            print(i, sentence.s, sentence.start_t, sentence.end_t)
            for letter in sentence.letters:
                print(' ', letter.character, letter.start_t, letter.end_t, letter.id, letter.width)

