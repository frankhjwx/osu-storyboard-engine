from funcy import flatten
import copy
from utils import *
from StoryboardCode import *


# Old Class, will be modified later
class Object:
    def __init__(self, file_name, type='Sprite', layer='Foreground', origin='Centre', x=320, y=240,
                 frame_count=0, frame_delay=0, loop_type=''):
        if not (type == 'Sprite' or type == 'Animation'):
            raise RuntimeError('No type supported for this kind of Object!')
        self.type = type
        self.layer = layer
        self.origin = origin
        self.file_name = '\"' + file_name + '\"'
        self.x = x
        self.y = y
        self.codes = []
        self.frame_count = frame_count
        self.frame_delay = frame_delay
        if type == 'Animation':
            if not (loop_type == 'LoopForever' or loop_type == 'LoopOnce'):
                raise RuntimeError('Not supported LoopType for animation.')
        self.loop_type = loop_type
        self.current_looplevel = 0

    def add(self, x):
        # if X is a Code
        if isinstance(x, Code):
            code = copy.deepcopy(x)
            self.codes.append(code)
            code.set_looplevel(self.current_looplevel)
            if code.key == 'T' or code.key == 'L':
                self.current_looplevel += 1
        # if X is a list of Codes
        if isinstance(x, list):
            codes = x
            for code in codes:
                self.codes.extend(code)
                code.set_looplevel(self.current_looplevel)
                if code.key == 'T' or code.key == 'L':
                    self.current_looplevel += 1

    def add_move(self, *args):
        args = array_to_list(args)
        # M,e,t1,t2,x1,y1,x2,y2
        if len(args) == 7:
            self.codes.append(Move(args[1:3], args[3:7], args[0], looplevel=self.current_looplevel))
        # M,0,t1,t2,x1,y1,x2,y2
        elif len(args) == 6:
            self.codes.append(Move(args[0:2], args[2:6], 0, looplevel=self.current_looplevel))
        # M,0,t1,t2,x1,y1
        elif len(args) == 4:
            self.codes.append(Move(args[0:2], args[2:4], 0, looplevel=self.current_looplevel))
        # M,0,t1,x1,y1
        elif len(args) == 3:
            self.codes.append(Move(args[0:1], args[1:3], 0, looplevel=self.current_looplevel))
        else:
            raise RuntimeError('Arg Num of Move Command is wrong.')

    def add_vector(self, *args):
        args = array_to_list(args)
        # V,e,t1,t2,x1,y1,x2,y2
        if len(args) == 7:
            self.codes.append(Vector(args[1:3], args[3:7], args[0], looplevel=self.current_looplevel))
        # V,0,t1,t2,x1,y1,x2,y2
        elif len(args) == 6:
            self.codes.append(Vector(args[0:2], args[2:6], 0, looplevel=self.current_looplevel))
        # V,0,t1,t2,x1,y1
        elif len(args) == 4:
            self.codes.append(Vector(args[0:2], args[2:4], 0, looplevel=self.current_looplevel))
        # V,0,t1,x1,y1
        elif len(args) == 3:
            self.codes.append(Vector(args[0:1], args[1:3], 0, looplevel=self.current_looplevel))
        else:
            raise RuntimeError('Arg Num of Vector Command is wrong.')

    def add_moveX(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(MoveX(args[1:3], args[3:5], args[0], looplevel=self.current_looplevel))
        elif len(args) == 4:
            self.codes.append(MoveX(args[0:2], args[2:4], 0, looplevel=self.current_looplevel))
        elif len(args) == 3:
            self.codes.append(MoveX(args[0:2], args[2:3], 0, looplevel=self.current_looplevel))
        elif len(args) == 2:
            self.codes.append(MoveX(args[0:1], args[1:2], 0, looplevel=self.current_looplevel))
        else:
            raise RuntimeError('Arg Num of MoveX Command is wrong.')

    def add_moveY(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(MoveY(args[1:3], args[3:5], args[0], looplevel=self.current_looplevel))
        elif len(args) == 4:
            self.codes.append(MoveY(args[0:2], args[2:4], 0, looplevel=self.current_looplevel))
        elif len(args) == 3:
            self.codes.append(MoveY(args[0:2], args[2:3], 0, looplevel=self.current_looplevel))
        elif len(args) == 2:
            self.codes.append(MoveY(args[0:1], args[1:2], 0, looplevel=self.current_looplevel))
        else:
            raise RuntimeError('Arg Num of MoveY Command is wrong.')

    def add_vectorX(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(VectorX(args[1:3], args[3:5], args[0], looplevel=self.current_looplevel))
        elif len(args) == 4:
            self.codes.append(VectorX(args[0:2], args[2:4], 0, looplevel=self.current_looplevel))
        elif len(args) == 3:
            self.codes.append(VectorX(args[0:2], args[2:3], 0, looplevel=self.current_looplevel))
        elif len(args) == 2:
            self.codes.append(VectorX(args[0:1], args[1:2], 0, looplevel=self.current_looplevel))
        else:
            raise RuntimeError('Arg Num of VectorX Command is wrong.')

    def add_vectorY(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(VectorY(args[1:3], args[3:5], args[0], looplevel=self.current_looplevel))
        elif len(args) == 4:
            self.codes.append(VectorY(args[0:2], args[2:4], 0, looplevel=self.current_looplevel))
        elif len(args) == 3:
            self.codes.append(VectorY(args[0:2], args[2:3], 0, looplevel=self.current_looplevel))
        elif len(args) == 2:
            self.codes.append(VectorY(args[0:1], args[1:2], 0, looplevel=self.current_looplevel))
        else:
            raise RuntimeError('Arg Num of VectorY Command is wrong.')

    def add_fade(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(Fade(args[1:3], args[3:5], args[0], looplevel=self.current_looplevel))
        elif len(args) == 4:
            self.codes.append(Fade(args[0:2], args[2:4], 0, looplevel=self.current_looplevel))
        elif len(args) == 3:
            self.codes.append(Fade(args[0:2], args[2:3], 0, looplevel=self.current_looplevel))
        elif len(args) == 2:
            self.codes.append(Fade(args[0:1], args[1:2], 0, looplevel=self.current_looplevel))
        else:
            raise RuntimeError('Arg Num of Fade Command is wrong.')

    def add_rotate(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(Rotate(args[1:3], args[3:5], args[0], looplevel=self.current_looplevel))
        elif len(args) == 4:
            self.codes.append(Rotate(args[0:2], args[2:4], 0, looplevel=self.current_looplevel))
        elif len(args) == 3:
            self.codes.append(Rotate(args[0:2], args[2:3], 0, looplevel=self.current_looplevel))
        elif len(args) == 2:
            self.codes.append(Rotate(args[0:1], args[1:2], 0, looplevel=self.current_looplevel))
        else:
            raise RuntimeError('Arg Num of Rotate Command is wrong.')

    def add_scale(self, *args):
        args = array_to_list(args)
        if len(args) == 5:
            self.codes.append(Rotate(args[1:3], args[3:5], args[0], looplevel=self.current_looplevel))
        elif len(args) == 4:
            self.codes.append(Scale(args[0:2], args[2:4], 0, looplevel=self.current_looplevel))
        elif len(args) == 3:
            self.codes.append(Scale(args[0:2], args[2:3], 0, looplevel=self.current_looplevel))
        elif len(args) == 2:
            self.codes.append(Scale(args[0:1], args[1:2], 0, looplevel=self.current_looplevel))
        else:
            raise RuntimeError('Arg Num of Scale Command is wrong.')

    def add_color(self, *args):
        args = array_to_list(args)
        if len(args) == 9:
            self.codes.append(Rotate(args[1:3], args[3:9], args[0], looplevel=self.current_looplevel))
        elif len(args) == 8:
            self.codes.append(Color(args[0:2], args[2:8], 0, looplevel=self.current_looplevel))
        elif len(args) == 5:
            self.codes.append(Color(args[0:2], args[2:5], 0, looplevel=self.current_looplevel))
        elif len(args) == 4:
            self.codes.append(Color(args[0:1], args[1:4], 0, looplevel=self.current_looplevel))
        else:
            raise RuntimeError('Arg Num of Color Command is wrong.')

    def add_parameter(self, *args):
        args = array_to_list(args)
        if len(args) == 4:
            self.codes.append(Parameter(args[1:3], args[3:4], args[0], looplevel=self.current_looplevel))
        elif len(args) == 3:
            self.codes.append(Parameter(args[0:2], args[2:3], 0, looplevel=self.current_looplevel))
        elif len(args) == 2:
            self.codes.append(Parameter(args[0:1], args[1:2], 0, looplevel=self.current_looplevel))
        else:
            raise RuntimeError('Arg Num of Parameter Command is wrong.')

    def add_loop(self, *args):
        args = array_to_list(args)
        if len(args) == 2:
            self.codes.append(Loop(args[0], args[1], looplevel=self.current_looplevel))
            self.current_looplevel += 1
        else:
            raise RuntimeError('Arg Num of Loop Command is wrong.')

    def add_loop_trigger(self, *args):
        args = array_to_list(args)
        if len(args) == 3:
            self.codes.append(Trigger(args[1:3], args[0], looplevel=self.current_looplevel))
            self.current_looplevel += 1
        else:
            raise RuntimeError('Arg Num of Trigger Command is wrong.')

    def loop_out(self):
        if self.current_looplevel > 0:
            self.current_looplevel -= 1
        else:
            raise RuntimeError('Not in any loop!')

    def remove(self, key):
        if key in code_arg_num:
            [self.codes.remove(code) for code in self.codes if code.key == key]
        else:
            raise RuntimeError('Not supported Command.')

    def remove_by_index(self, index):
        '''Remove a Code object in codes list. Count from index 1.'''
        if index <= len(self.codes):
            del self.codes[index - 1]
        else:
            raise RuntimeError('Not in codes list.')

    def print_object(self, file_header=None):
        if self.type == 'Sprite':
            obj_header = ','.join(
                [self.type, self.layer, self.origin, self.file_name, str(self.x), str(self.y)])
        else:
            obj_header = ','.join(
                [self.type, self.layer, self.origin, self.file_name, str(self.x), str(self.y),
                 str(self.frame_count), str(self.frame_delay), str(self.loop_type)])
        if file_header == None:
            print(obj_header)
            for code in self.codes:
                print(code)
        else:
            file_header.write(obj_header + '\n')
            for code in self.codes:
                file_header.write(code.get_string() + '\n')


def ObjTest():
    Red = [255, 0, 0]
    White = [255, 255, 255]

    obj = Object('star.png', type='Animation', frame_count=24, frame_delay=40, loop_type='LoopOnce')
    obj.add_move('00:23:345', 320, 240)
    obj.add_rotate('00:24:560', '00:26:402', 1, 30.234)
    obj.add_fade('00:25:400', '00:30:300', 1, 0)
    obj.add_loop_trigger('Hitsound', 30000, 40000)
    obj.add_vector(0, 0, 0)
    obj.loop_out()
    obj.add_color('00:23:345', Red)
    obj.remove_by_index(2)
    obj.print_object()
