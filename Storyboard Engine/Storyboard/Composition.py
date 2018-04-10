from Storyboard.StoryboardObject import *

# Still under development


class Composition:
    # unfinish
    def __init__(self, timing_offset=0, position_offset=0):
        self.list = []
        self.timing_offset = timing_offset
        self.position_offset = None
        self.set_position_offset(position_offset)


    def add_object(self, *args):
        for arg in args:
            self.list.append(arg)

    def set_timing_offset(self, ms):
        self.timing_offset = ms

    def set_position_offset(self, vector):
        if isinstance(vector, list):
            self.position_offset = vector
        elif isinstance(vector, (int, float)):
            self.position_offset = [vector, vector]

    def apply_change(self):
        conut = 0
        for obj in self.list:
            if self.position_offset != None:
                obj.x = obj.x + self.position_offset[0]
                obj.y = obj.y + self.position_offset[1]
            for code in obj.codes:
                code.timing[0] = code.timing[0] + self.timing_offset
                if not (code.timing[1] == None or code.timing[1] == ''):
                    code.timing[1] = code.timing[1] + self.timing_offset
                if isinstance(code, Move):
                    code.data[0] += self.position_offset[0]
                    code.data[1] += self.position_offset[1]
                    if len(code.data) == 4:
                        code.data[2] += self.position_offset[0]
                        code.data[3] += self.position_offset[1]

    def clone(self):
        "Return a new same Composition Object"
        return copy.deepcopy(self)

    def print_all(self, file_header=None):
        for obj in self.list:
            obj.print_object(file_header)


if __name__ == '__main__':
    obj = Object('star.png', object_type='Animation', frame_count=24, frame_delay=40, loop_type='LoopOnce')
    obj.add_move('00:23:345', 320, 240)
    obj.add_rotate('00:24:560', '00:26:402', 1, 30.234)
    obj.add_fade('00:25:400', '00:30:300', 1, 0)
    obj.add_loop_trigger('Hitsound', 30000, 40000)
    obj.add_vector(0, 0, 0)
    obj.loop_out()
    obj.add_color('00:23:345', [255,0,0])

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
