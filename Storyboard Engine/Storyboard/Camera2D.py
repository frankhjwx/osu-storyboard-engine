from tools.easingFuncs import *
from tools.utils import *
from Storyboard.StoryboardCode import *


MIN_T = 1145141919810


class Camera2D:
    def __init__(self, pos_x=320, pos_y=240, scale=1, rotate=0, frame_per_second=20):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.scale = scale
        self.rotate = rotate
        self.codes = []
        self.fps = frame_per_second
        self.start_t = MIN_T
        self.end_t = -MIN_T

    def Move(self, *args):
        args = array_to_list(args)
        # M,e,t1,t2,x1,y1,x2,y2
        if len(args) == 7:
            self.codes.append(Move(args[1:3], args[3:7], args[0], loop_level=0))
        # M,0,t1,t2,x1,y1,x2,y2
        elif len(args) == 6:
            self.codes.append(Move(args[0:2], args[2:6], 0, loop_level=0))
        # M,0,t1,t2,x1,y1
        elif len(args) == 4:
            self.codes.append(Move(args[0:2], args[2:4], 0, loop_level=0))
        # M,0,t1,x1,y1
        elif len(args) == 3:
            self.codes.append(Move(args[0:1], args[1:3], 0, loop_level=0))
        else:
            raise RuntimeError('Arg Num of Move Command is wrong.')

    def Scale(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(Scale(args[1:3], args[3:5], args[0], loop_level=0))
        elif len(args) == 4:
            self.codes.append(Scale(args[0:2], args[2:4], 0, loop_level=0))
        elif len(args) == 3:
            self.codes.append(Scale(args[0:2], args[2:3], 0, loop_level=0))
        elif len(args) == 2:
            self.codes.append(Scale(args[0:1], args[1:2], 0, loop_level=0))
        else:
            raise RuntimeError('Arg Num of Scale Command is wrong.')

    def Rotate(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(Rotate(args[1:3], args[3:5], args[0], loop_level=0))
        elif len(args) == 4:
            self.codes.append(Rotate(args[0:2], args[2:4], 0, loop_level=0))
        elif len(args) == 3:
            self.codes.append(Rotate(args[0:2], args[2:3], 0, loop_level=0))
        elif len(args) == 2:
            self.codes.append(Rotate(args[0:1], args[1:2], 0, loop_level=0))
        else:
            raise RuntimeError('Arg Num of Rotate Command is wrong.')

    def get_start_end_t(self):
        for code in self.codes:
            if code.timing[0] < self.start_t:
                self.start_t = code.timing[0]
                if self.end_t == -MIN_T:
                    self.end_t = code.timing[0]
            if code.timing[1] != '' and code.timing[1] > self.end_t:
                self.end_t = code.timing[1]

    def get_status(self, timing):
        self.get_start_end_t()
        status = {}
        for key in code_arg_num:
            code_list = [code for code in self.codes if code.key == key]
            if code_list == []:
                status[key] = None
            else:
                status[key] = self.get_status_key(key, timing, code_list)
        return status

    def get_status_key(self, key, timing, code_list):
        if timing < self.start_t:
            timing = self.start_t
        if timing > self.end_t:
            timing = self.end_t
        code_list = sorted(code_list, key=lambda c: c.timing[0])
        for code in code_list:
            if timing <= code.timing[0]:
                return code.data[0:code_arg_num[key]]
            if code.timing[1] != '' and code.timing[0] < timing < code.timing[1]:
                start_v = code.data[0:code_arg_num[key]]
                if len(code.data) > code_arg_num[key]:
                    end_v = code.data[code_arg_num[key]:len(code.data)]
                else:
                    end_v = start_v
                start_v = [float(v) for v in start_v]
                end_v = [float(v) for v in end_v]
                return self.get_easing_value(code.easing, code.timing[0], code.timing[1], start_v, end_v, timing)
        code = code_list[len(code_list) - 1]
        start_v = code.data[0:code_arg_num[key]]
        if len(code.data) > code_arg_num[key]:
            end_v = code.data[code_arg_num[key]:len(code.data)]
        else:
            end_v = start_v
        return end_v

    def get_easing_value(self, easing, start_t, end_t, start_v, end_v, timing):
        t = (timing - start_t) / (end_t - start_t)
        value = [start_v[i] + numToEasing[easing](t)*(end_v[i]-start_v[i]) for i in range(len(start_v))]
        return value

    def get_position(self, timing):
        status = self.get_status(timing)
        pos = [self.pos_x, self.pos_y]
        if status['M'] is not None:
            pos = status['M']
        return pos

    def get_scale(self, timing):
        status = self.get_status(timing)
        scale = self.scale
        if status['S'] is not None:
            scale = status['S'][0]
        return scale

    def get_rotation(self, timing):
        status = self.get_status(timing)
        rotation = self.rotate
        if status['R'] is not None:
            rotation = status['R'][0]
        return rotation

if __name__ == '__main__':
    cam = Camera2D()
    cam.Move(1000, 2400, 300, 240, 340, 240)
    for i in range(1000, 2500, 100):
        print(i, cam.get_position(i), cam.get_scale(i), cam.get_rotation(i), cam.get_status(i))
