import copy
from StoryboardCode import *
from StoryboardObject import *

class Composition():
    # unfinish
    def __init__(self, timing_offset=0, position_offset=0):
        self.list = []
        self.timingOffset = timing_offset
        self.positionOffset = None
        self.set_position_offset(position_offset)


    def add_object(self, *args):
        for arg in args:
            self.list.append(arg)

    def set_timing_offset(self, ms):
        self.timingOffset = ms

    def set_position_offset(self, vector):
        if isinstance(vector, list):
            self.positionOffset = vector
        elif isinstance(vector, (int, float)):
            self.positionOffset = [vector, vector]

    def apply_change(self):
        conut = 0
        for obj in self.list:
            if self.positionOffset != None:
                obj.x = obj.x + self.positionOffset[0]
                obj.y = obj.y + self.positionOffset[1]
            for code in obj.codes:
                code.timing[0] = code.timing[0] + self.timingOffset
                if not (code.timing[1] == None or code.timing[1] == ''):
                    code.timing[1] = code.timing[1] + self.timingOffset
                if isinstance(code, Move):
                    code.data[0] += self.positionOffset[0]
                    code.data[1] += self.positionOffset[1]
                    if len(code.data) == 4:
                        code.data[2] += self.positionOffset[0]
                        code.data[3] += self.positionOffset[1]

    def clone(self):
        "Return a new same Composition Object"
        return copy.deepcopy(self)

    def print_all(self):
        for obj in self.list:
            obj.print_obj()

obj = Object('star.png', type='Animation', frameCount=24, frameDelay=40, loopType='LoopOnce')
obj.Move('00:23:345', 320, 240)
obj.Rotate('00:24:560', '00:26:402', 1, 30.234)
obj.Fade('00:25:400', '00:30:300', 1, 0)
obj.Trigger('Hitsound', 30000, 40000)
obj.Vector(0, 0, 0)
obj.LoopOut()
obj.Color('00:23:345', [255,0,0])

obj2 = copy.deepcopy(obj)

comp = Composition()
comp.add_object(obj)
comp.add_object(obj2)
comp.print_all()

comp2 = comp.clone()
comp2.set_timing_offset(123)
comp2.set_position_offset(100)
comp2.apply_change()
comp2.print_all()