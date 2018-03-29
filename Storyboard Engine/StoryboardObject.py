from funcy import flatten
import copy
from utils import *
from StoryboardCode import *


# Old Class, will be modified later
class Object:
    def __init__(self, file_name, type='Sprite', origin='Centre', x=320, y=240,
                 frameCount=0, frameDelay=0, loopType=''):
        if not (type == 'Sprite' or type == 'Animation'):
            raise RuntimeError('No type supported for this kind of Object!')
        self.type = type
        self.layer = 'Foreground'
        self.origin = origin
        self.fileName = '\"' + file_name + '\"'
        self.x = x
        self.y = y
        self.codes = []
        self.frameCount = frameCount
        self.frameDelay = frameDelay
        if type == 'Animation':
            if not (loopType == 'LoopForever' or loopType == 'LoopOnce'):
                raise RuntimeError('Not supported LoopType for animation.')
        self.loopType = loopType
        self.currentLoopLevel = 0

    def add(self, x):
        # if X is a Code
        if isinstance(x, Code):
            code = copy.deepcopy(x)
            self.codes.append(code)
            code.set_looplevel(self.currentLoopLevel)
            if code.key == 'T' or code.key == 'L':
                self.currentLoopLevel += 1
        # if X is a list of Codes
        if isinstance(x, list):
            codes = x
            for code in codes:
                self.codes.extend(code)
                code.set_looplevel(self.currentLoopLevel)
                if code.key == 'T' or code.key == 'L':
                    self.currentLoopLevel += 1

    def Move(self, *args, easing=0):
        if len(args) == 6:
            self.codes.append(Move(args[0:2], args[2:6], easing, looplevel=self.currentLoopLevel))
        if len(args) == 4:
            self.codes.append(Move(args[0:2], args[2:4], easing, looplevel=self.currentLoopLevel))
        if len(args) == 3:
            self.codes.append(Move(args[0:1], args[1:3], easing, looplevel=self.currentLoopLevel))

    def Vector(self, *args, easing=0):
        if len(args) == 6:
            self.codes.append(Vector(args[0:2], args[2:6], looplevel=self.currentLoopLevel))
        if len(args) == 4:
            self.codes.append(Vector(args[0:2], args[2:4], easing, looplevel=self.currentLoopLevel))
        if len(args) == 3:
            self.codes.append(Vector(args[0:1], args[1:3], easing, looplevel=self.currentLoopLevel))

    def MoveX(self, *args, easing=0):
        if len(args) == 4:
            self.codes.append(MoveX(args[0:2], args[2:4], easing, looplevel=self.currentLoopLevel))
        if len(args) == 3:
            self.codes.append(MoveX(args[0:2], args[2:3], easing, looplevel=self.currentLoopLevel))
        if len(args) == 2:
            self.codes.append(MoveX(args[0:1], args[1:2], easing, looplevel=self.currentLoopLevel))

    def MoveY(self, *args, easing=0):
        if len(args) == 4:
            self.codes.append(MoveY(args[0:2], args[2:4], easing, looplevel=self.currentLoopLevel))
        if len(args) == 3:
            self.codes.append(MoveY(args[0:2], args[2:3], easing, looplevel=self.currentLoopLevel))
        if len(args) == 2:
            self.codes.append(MoveY(args[0:1], args[1:2], easing, looplevel=self.currentLoopLevel))

    def VectorX(self, *args, easing=0):
        if len(args) == 4:
            self.codes.append(VectorX(args[0:2], args[2:4], easing, looplevel=self.currentLoopLevel))
        if len(args) == 3:
            self.codes.append(VectorX(args[0:2], args[2:3], easing, looplevel=self.currentLoopLevel))
        if len(args) == 2:
            self.codes.append(VectorX(args[0:1], args[1:2], easing, looplevel=self.currentLoopLevel))

    def VectorY(self, *args, easing=0):
        if len(args) == 4:
            self.codes.append(VectorY(args[0:2], args[2:4], easing, looplevel=self.currentLoopLevel))
        if len(args) == 3:
            self.codes.append(VectorY(args[0:2], args[2:3], easing, looplevel=self.currentLoopLevel))
        if len(args) == 2:
            self.codes.append(VectorY(args[0:1], args[1:2], easing, looplevel=self.currentLoopLevel))

    def Fade(self, *args, easing=0):
        if len(args) == 4:
            self.codes.append(Fade(args[0:2], args[2:4], easing, looplevel=self.currentLoopLevel))
        if len(args) == 3:
            self.codes.append(Fade(args[0:2], args[2:3], easing, looplevel=self.currentLoopLevel))
        if len(args) == 2:
            self.codes.append(Fade(args[0:1], args[1:2], easing, looplevel=self.currentLoopLevel))

    def Rotate(self, *args, easing=0):
        if len(args) == 4:
            self.codes.append(Rotate(args[0:2], args[2:4], easing, looplevel=self.currentLoopLevel))
        if len(args) == 3:
            self.codes.append(Rotate(args[0:2], args[2:3], easing, looplevel=self.currentLoopLevel))
        if len(args) == 2:
            self.codes.append(Rotate(args[0:1], args[1:2], easing, looplevel=self.currentLoopLevel))

    def Scale(self, *args, easing=0):
        if len(args) == 4:
            self.codes.append(Scale(args[0:2], args[2:4], easing, looplevel=self.currentLoopLevel))
        if len(args) == 3:
            self.codes.append(Scale(args[0:2], args[2:3], easing, looplevel=self.currentLoopLevel))
        if len(args) == 2:
            self.codes.append(Scale(args[0:1], args[1:2], easing, looplevel=self.currentLoopLevel))

    def Color(self, *args, easing=0):
        args = array_to_list(args)
        if len(args) == 8:
            self.codes.append(Color(args[0:2], args[2:8], easing, looplevel=self.currentLoopLevel))
        if len(args) == 5:
            self.codes.append(Color(args[0:2], args[2:5], easing, looplevel=self.currentLoopLevel))
        if len(args) == 4:
            self.codes.append(Color(args[0:1], args[1:4], easing, looplevel=self.currentLoopLevel))

    def Parameter(self, *args, easing=0):
        if len(args) == 3:
            self.codes.append(Parameter(args[0:2], args[2:3], easing, looplevel=self.currentLoopLevel))
        if len(args) == 2:
            self.codes.append(Parameter(args[0:1], args[1:2], easing, looplevel=self.currentLoopLevel))

    def Loop(self, *args):
        if len(args) == 2:
            self.codes.append(Loop(args[0], args[1], looplevel=self.currentLoopLevel))
            self.currentLoopLevel += 1

    def Trigger(self, *args):
        if len(args) == 3:
            self.codes.append(Trigger(args[1:3], args[0], looplevel=self.currentLoopLevel))
            self.currentLoopLevel += 1

    def LoopOut(self):
        self.currentLoopLevel -= 1

    def print_obj(self):
        if self.type == 'Sprite':
            objHeader = ','.join(
                [self.type, self.layer, self.origin, self.fileName, str(self.x), str(self.y)])
        else:
            objHeader = ','.join(
                [self.type, self.layer, self.origin, self.fileName, str(self.x), str(self.y),
                 str(self.frameCount), str(self.frameDelay), str(self.loopType)])
        print(objHeader)
        for code in self.codes:
            abc = code.__str__()
            tmp_str = tmp_str + (inner_space + abc) + '\n'
        return tmp_str


def ObjTest():
    Red = [255, 0, 0]
    White = [255, 255, 255]

    obj = Object('star.png', type='Animation', frameCount=24, frameDelay=40, loopType='LoopOnce')
    obj.Move('00:23:345', 320, 240)
    obj.Rotate('00:24:560', '00:26:402', 1, 30.234)
    obj.Fade('00:25:400', '00:30:300', 1, 0)
    obj.Trigger('Hitsound', 30000, 40000)
    obj.Vector(0, 0, 0)
    obj.LoopOut()
    obj.Color('00:23:345', Red)
    obj.print_obj()
