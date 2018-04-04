from funcy import flatten
import copy
from utils import *
from StoryboardCode import *


# Old Class, will be modified later
class Object:
    def __init__(self, file_name, layer='Foreground', type='Sprite', origin='Centre', x=320, y=240,
                 frameCount=0, frameDelay=0, loopType=''):
        if not (type == 'Sprite' or type == 'Animation'):
            raise RuntimeError('No type supported for this kind of Object!')
        self.type = type
        self.layer = layer
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

    def Move(self, *args):
        args = array_to_list(args)
        # M,e,t1,t2,x1,y1,x2,y2
        if len(args) == 7:
            self.codes.append(Move(args[1:3], args[3:7], args[0], looplevel=self.currentLoopLevel))
        # M,0,t1,t2,x1,y1,x2,y2
        elif len(args) == 6:
            self.codes.append(Move(args[0:2], args[2:6], 0, looplevel=self.currentLoopLevel))
        # M,0,t1,t2,x1,y1
        elif len(args) == 4:
            self.codes.append(Move(args[0:2], args[2:4], 0, looplevel=self.currentLoopLevel))
        # M,0,t1,x1,y1
        elif len(args) == 3:
            self.codes.append(Move(args[0:1], args[1:3], 0, looplevel=self.currentLoopLevel))
        else:
            raise RuntimeError('Arg Num of Move Command is wrong.')

    def Vector(self, *args):
        args = array_to_list(args)
        # V,e,t1,t2,x1,y1,x2,y2
        if len(args) == 7:
            self.codes.append(Vector(args[1:3], args[3:7], args[0], looplevel=self.currentLoopLevel))
        # V,0,t1,t2,x1,y1,x2,y2
        elif len(args) == 6:
            self.codes.append(Vector(args[0:2], args[2:6], 0, looplevel=self.currentLoopLevel))
        # V,0,t1,t2,x1,y1
        elif len(args) == 4:
            self.codes.append(Vector(args[0:2], args[2:4], 0, looplevel=self.currentLoopLevel))
        # V,0,t1,x1,y1
        elif len(args) == 3:
            self.codes.append(Vector(args[0:1], args[1:3], 0, looplevel=self.currentLoopLevel))
        else:
            raise RuntimeError('Arg Num of Vector Command is wrong.')

    def MoveX(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(MoveX(args[1:3], args[3:5], args[0], looplevel=self.currentLoopLevel))
        elif len(args) == 4:
            self.codes.append(MoveX(args[0:2], args[2:4], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 3:
            self.codes.append(MoveX(args[0:2], args[2:3], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 2:
            self.codes.append(MoveX(args[0:1], args[1:2], 0, looplevel=self.currentLoopLevel))
        else:
            raise RuntimeError('Arg Num of MoveX Command is wrong.')

    def MoveY(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(MoveY(args[1:3], args[3:5], args[0], looplevel=self.currentLoopLevel))
        elif len(args) == 4:
            self.codes.append(MoveY(args[0:2], args[2:4], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 3:
            self.codes.append(MoveY(args[0:2], args[2:3], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 2:
            self.codes.append(MoveY(args[0:1], args[1:2], 0, looplevel=self.currentLoopLevel))
        else:
            raise RuntimeError('Arg Num of MoveY Command is wrong.')

    def VectorX(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(VectorX(args[1:3], args[3:5], args[0], looplevel=self.currentLoopLevel))
        elif len(args) == 4:
            self.codes.append(VectorX(args[0:2], args[2:4], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 3:
            self.codes.append(VectorX(args[0:2], args[2:3], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 2:
            self.codes.append(VectorX(args[0:1], args[1:2], 0, looplevel=self.currentLoopLevel))
        else:
            raise RuntimeError('Arg Num of VectorX Command is wrong.')

    def VectorY(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(VectorY(args[1:3], args[3:5], args[0], looplevel=self.currentLoopLevel))
        elif len(args) == 4:
            self.codes.append(VectorY(args[0:2], args[2:4], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 3:
            self.codes.append(VectorY(args[0:2], args[2:3], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 2:
            self.codes.append(VectorY(args[0:1], args[1:2], 0, looplevel=self.currentLoopLevel))
        else:
            raise RuntimeError('Arg Num of VectorY Command is wrong.')

    def Fade(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(Fade(args[1:3], args[3:5], args[0], looplevel=self.currentLoopLevel))
        elif len(args) == 4:
            self.codes.append(Fade(args[0:2], args[2:4], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 3:
            self.codes.append(Fade(args[0:2], args[2:3], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 2:
            self.codes.append(Fade(args[0:1], args[1:2], 0, looplevel=self.currentLoopLevel))
        else:
            raise RuntimeError('Arg Num of Fade Command is wrong.')

    def Rotate(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(Rotate(args[1:3], args[3:5], args[0], looplevel=self.currentLoopLevel))
        elif len(args) == 4:
            self.codes.append(Rotate(args[0:2], args[2:4], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 3:
            self.codes.append(Rotate(args[0:2], args[2:3], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 2:
            self.codes.append(Rotate(args[0:1], args[1:2], 0, looplevel=self.currentLoopLevel))
        else:
            raise RuntimeError('Arg Num of Rotate Command is wrong.')

    def Scale(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(Rotate(args[1:3], args[3:5], args[0], looplevel=self.currentLoopLevel))
        elif len(args) == 4:
            self.codes.append(Scale(args[0:2], args[2:4], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 3:
            self.codes.append(Scale(args[0:2], args[2:3], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 2:
            self.codes.append(Scale(args[0:1], args[1:2], 0, looplevel=self.currentLoopLevel))
        else:
            raise RuntimeError('Arg Num of Scale Command is wrong.')

    def Color(self, *args):
        args = array_to_list(args)
        if len(args) == 9:
            self.codes.append(Rotate(args[1:3], args[3:9], args[0], looplevel=self.currentLoopLevel))
        elif len(args) == 8:
            self.codes.append(Color(args[0:2], args[2:8], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 5:
            self.codes.append(Color(args[0:2], args[2:5], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 4:
            self.codes.append(Color(args[0:1], args[1:4], 0, looplevel=self.currentLoopLevel))
        else:
            raise RuntimeError('Arg Num of Color Command is wrong.')

    def Parameter(self, *args):
        args = array_to_list(args)
        if len(args) == 4:
            self.codes.append(Parameter(args[1:3], args[3:4], args[0], looplevel=self.currentLoopLevel))
        elif len(args) == 3:
            self.codes.append(Parameter(args[0:2], args[2:3], 0, looplevel=self.currentLoopLevel))
        elif len(args) == 2:
            self.codes.append(Parameter(args[0:1], args[1:2], 0, looplevel=self.currentLoopLevel))
        else:
            raise RuntimeError('Arg Num of Parameter Command is wrong.')

    def Loop(self, *args):
        args = array_to_list(args)
        if len(args) == 2:
            self.codes.append(Loop(args[0], args[1], looplevel=self.currentLoopLevel))
            self.currentLoopLevel += 1
        else:
            raise RuntimeError('Arg Num of Loop Command is wrong.')

    def Trigger(self, *args):
        args = array_to_list(args)
        if len(args) == 3:
            self.codes.append(Trigger(args[1:3], args[0], looplevel=self.currentLoopLevel))
            self.currentLoopLevel += 1
        else:
            raise RuntimeError('Arg Num of Trigger Command is wrong.')

    def LoopOut(self):
        if self.currentLoopLevel > 0:
            self.currentLoopLevel -= 1
        else:
            raise RuntimeError('Not in any loop!')

    def printObject(self):
        if self.type == 'Sprite':
            objHeader = ','.join(
                [self.type, self.layer, self.origin, self.fileName, str(self.x), str(self.y)])
        else:
            objHeader = ','.join(
                [self.type, self.layer, self.origin, self.fileName, str(self.x), str(self.y),
                 str(self.frameCount), str(self.frameDelay), str(self.loopType)])
        print(objHeader)
        for code in self.codes:
            print(code)


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
    obj.printObject()
