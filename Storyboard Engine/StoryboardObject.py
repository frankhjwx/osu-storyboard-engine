from funcy import flatten
import copy
from utils import time_parser
from StoryboardCode import *


# Old Class, will be modified later
class Object:
    def __init__(self, file_name, alignment='Centre', x=320, y=240):
        self.type = 'Sprite'
        self.placement = 'Foreground'
        self.alignment = alignment
        self.fileName = '\"' + file_name + '\"'
        self.x = x
        self.y = y
        self.codes = []
        self.currentLoopLevel = 1

    def add(self, x):
        # if X is a Code
        if isinstance(x, Code):
            code = copy.deepcopy(x)
            self.codes.append(code)
            code.set_loop_level(self.currentLoopLevel)
            if code.key == 'T' or code.key == 'L':
                self.currentLoopLevel += 1
        # if X is a list of Codes
        if isinstance(x, list):
            codes = x
            self.codes.extend(codes)
            for code in codes:
                code.set_loop_level(self.currentLoopLevel)
                if code.key == 'T' or code.key == 'L':
                    self.currentLoopLevel += 1

    def loop_out(self):
        self.currentLoopLevel -= 1

    def print_obj(self):
        self.codes.insert(0, ','.join(
            [self.type, self.placement, self.alignment, self.fileName, str(self.x), str(self.y)]))
        for code in self.codes:
            print(code)


def ObjTest():
    Red = [255, 0, 0]
    White = [255, 255, 255]

    mov = Move(123, [123, 345])
    mov2 = Move([12, 34], [1, 2, 1, 2])
    mov3 = Move(1, [123, 324, 234, 234])
    color = Color(['1:02:323', '2:53:23'], [Red, White])
    print(color)
    trigger = Trigger([123, 234], 'Hitsound')
    trigger2 = Trigger([123, 345], 'HitsoundSoftClap')
    loop = Loop(123, 30)
    loop2 = Loop([234], 30)
    loop3 = Loop('599', 30)
    print(trigger)

    obj = Object('star.png')
    obj.add(mov)
    obj.add(mov)
    obj.add(trigger)
    obj.add(mov2)
    obj.add(trigger2)
    obj.add(mov2)
    obj.loop_out()
    obj.loop_out()
    obj.add(color)
    obj.add(mov3)
    obj.add(loop)
    obj.add(color)
    obj.loop_out()
    obj.print_obj()

ObjTest()