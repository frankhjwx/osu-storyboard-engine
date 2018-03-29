from funcy import flatten
import copy

codeArgNum = {
    'M' :    2, 'F'  :     1,  'S'  :    1,
    'V' :    2, 'MX' :     1,  'MY' :    1,
    'VX':    1, 'VY' :     1,  'R'  :    1,
    'C' :    3, 'P'  :     1
}


def command(*args):
    s = ','.join(str(arg) for arg in args)
    return s


def time_parser(s):
    args = s.split(':')
    m = int(args[0])
    s = int(args[1])
    ms = int(args[2])
    if not (0 <= 59 and 0 <= ms <= 999):
        raise RuntimeError('Wrong Timing Format.')
    return (m * 60 + s) * 1000 + ms


def get_timing(start_t, end_t=''):
    """Return a list like [start_t, end_t], end_t default value is a empty."""
    return [start_t, end_t]


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
        self.currentLoopLevel = 0
        self.isLooping = False
        self.isTriggering = False
        self.isInnerClass = False
        self.loop = Loop
        # self.codes.append(','.join(
        # [self.type, self.placement, self.alignment, self.filename, str(self.x), str(self.y)]))

    def add(self, x):
        if not self.isLooping:
            # if X is a Code
            if isinstance(x, Code):
                self.codes.append(x)
            # if X is a list of Codes
            if isinstance(x, list):
                self.codes.extend(x)
        elif self.isLooping:
            self.loop.codes.append(x)

        # elif self.isTriggering:
        #   self.trigger.codes.append(x)

    def start_trigger(self, condition, start_t, end_t):
        if self.isLooping or self.isTriggering:
            raise RuntimeError('You can not start another loop when the previous one isn\'t end.')
        self.currentLoopLevel += 1
        # spaces = ' ' * self.currentLoopLevel
        # c = spaces + 'T'
        # self.codes.append(command(c, condition, start_t, end_t))

    def start_loop(self, start_t, loop_count):
        if self.isLooping or self.isTriggering:
            raise RuntimeError('You can not start another loop when the previous one isn\'t end.')
        self.currentLoopLevel += 1
        self.isLooping = True
        self.loop = Loop(start_t, loop_count)
        # spaces = ' ' * self.currentLoopLevel
        # c = spaces + 'L'
        # self.codes.append(command(c, start_t, loop_count))

    def end_loop(self):
        if not self.isLooping and not self.isTriggering:
            raise RuntimeError('You can not stop a loop when a loop isn\'t started.')
        self.codes.append(self.loop)
        self.isLooping = False
        self.isTriggering = False
        self.currentLoopLevel -= 1

    # def add(self, s):
    #     self.codes.append(s)

    def print_obj(self):
        ','.join([self.type, self.placement, self.alignment, self.fileName, str(self.x), str(self.y)])
        abc = self.__str__()
        print(','.join(
            [self.type, self.placement, self.alignment, self.fileName, str(self.x),
             str(self.y)]) + "\n" + abc)
        # inner_space = ''
        # if self.isInnerClass:
        #    inner_space = ' '
        # if not self.isInnerClass:
        #    self.codes.insert(0, ','.join(
        #        [self.type, self.placement, self.alignment, self.fileName, str(self.x), str(self.y)]))
        # for code in self.codes:
        #    print(inner_space + code.get_string())

    def __str__(self):
        tmp_str = ''
        inner_space = ''
        if self.isInnerClass:
            inner_space = ' '

        for code in self.codes:
            abc = code.__str__()
            tmp_str = tmp_str + (inner_space + abc) + '\n'
        return tmp_str


class Code(object):
    def array_to_list(self, l, a=None):
        a = list(a) if isinstance(a, (list, tuple)) else []
        for i in l:
            if isinstance(i, (list, tuple)):
                a = self.array_to_list(i, a)
            else:
                a.append(i)
        return a

    @staticmethod
    def normalize_timing_format(t):
        if isinstance(t, str):
            ts = t.split(':')
            if len(ts) == 1:
                return int(ts)
            elif len(ts) == 3:
                return time_parser(t)
            else:
                raise RuntimeError('Wrong Timing Format.')
        else:
            return int(t)

    def __init__(self, key, timing, data, easing=0, loop_level=1):
        """Init must take keyword, timing(If it's dict, please write like {\"start_t\": [value], \"end_t\": [value]}. \
        If it's list, please keep two values), data. If you need, write down easing = [value] to change easing value."""
        # Do format check
        data = self.array_to_list(data)
        if key not in codeArgNum:
            raise RuntimeError(key + 'command is not supported in this system!')
        if not (isinstance(easing, int) and 0 <= easing <= 34):
            raise RuntimeError('Easing wrongly set.')

        self.key = key
        self.easing = easing
        if isinstance(timing, tuple):
            timing = list(timing)
        if isinstance(timing, list):
            if len(timing) == 0 or len(timing) > 2:
                raise RuntimeError('Not supported timing argument.')
            if len(timing) == 1:
                self.timing = get_timing(timing[0])
            else:
                self.timing = get_timing(timing[0], timing[1])
        elif isinstance(timing, dict):
            if not ('start_t' in timing and 'end_t' in timing):
                raise RuntimeError('Not supported timing argument.')
            self.timing = get_timing(timing['start_t'], timing['end_t'])
        else:
            self.timing = get_timing(timing)
        self.timing[0] = self.normalize_timing_format(self.timing[0])
        if self.timing[1] != '':
            self.timing[1] = self.normalize_timing_format(self.timing[1])
        if len(data) % codeArgNum[self.key] == 0:
            if len(data) / codeArgNum[self.key] == 2:
                data1 = data[:codeArgNum[self.key]]
                data2 = data[codeArgNum[self.key]:]
                if data1 == data2:
                    data = data1
            self.data = data
        else:
            raise RuntimeError('Command data set wrongly, please recheck your code.')
        self.loopLevel = loop_level

    def change_loop_level(self, loop_level):
        self.loopLevel = loop_level

    def get_list(self):
        """Return a list look like [key, easing, start_t, end_t, *data]"""
        return flatten([self.key, self.easing, self.timing, self.data])

    def get_string(self):
        """Return a string look like \' M,0,123,456,123,345 \'"""
        return self.loopLevel * ' ' + ','.join(map(str, self.get_list()))

    def __str__(self):
        return self.get_string()

    __repr__ = __str__


class Move(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'M', timing, data, easing=easing)


class MoveX(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'MX', timing, data, easing=easing)


class MoveY(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'MY', timing, data, easing=easing)


class Fade(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'F', timing, data, easing=easing)


class Scale(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'S', timing, data, easing)


class Vector(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'V', timing, data, easing)


class VectorX(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'VX', timing, data, easing)


class VectorY(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'VY', timing, data, easing)


class Rotate(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'R', timing, data, easing=easing)


class Color(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'C', timing, data, easing=easing)

class Loop(object):
    def __init__(self, start_time, loop_count):
        self.startTime = start_time
        self.isLooping = False
        self.loopCount = loop_count
        self.isInnerClass = True
        self.codes = []
        # self.codes.append(','.join(
        # [self.type, self.placement, self.alignment, self.filename, str(self.x), str(self.y)]))

    def __str__(self):
        tmp_str = ' L,' + str(self.startTime) + ',' + str(self.loopCount) + '\n' + Object.__str__(self)
        return tmp_str

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
        elif isinstance(vector, (int, long, float)):
            self.positionOffset = [vector, vector]

    def apply_change(self):
        conut = 0
        for obj in self.list:
            if self.positionOffset != None:
                obj.x = obj.x + self.positionOffset[0]
                obj.y = obj.y + self.positionOffset[1]
            for code in obj.codes:
                code.timing[0] = code.timing[0] + self.timingOffset
                if code.timing[1] != None:
                    code.timing[1] = code.timing[1] + self.timingOffset
                if isinstance(code, Move):
                    code.data[0] += self.positionOffset[0]
                    code.data[1] += self.positionOffset[1]
                    code.data[2] += self.positionOffset[0]
                    code.data[3] += self.positionOffset[1]

    def clone(self):
        "Return a new same Composition Object"
        return copy.deepcopy(self)

    def print_all(self):
        for obj in self.list:
            obj.print_obj()


# Usage
# Declare a new Object
# Obj = Object('exampleFile.png')
# # addM args: easing, start_t, (end_t), start_x, start_y, (end_x), (end_y)
# Obj.addM(0, 1234, 1235, 0, 0, 320, 240)
# # addT args: condition, start_t, end_t
# # WARNING: When using addT and addL operations, looplevel will +1 by default,
# # to exit the loop, you should use LoopOut Command
# Obj.startTrigger('HitSound', 2000, 2018)
# Obj.addF(0, 0, 500, 0, 1)
# Obj.addF(0, 1000, 1500, 1, 0)
# Obj.LoopOut()
# Obj.addP(0, 1200, 'A')
# Obj.addC(0, 1000, 255, 255, 255)


# Obj.printObj()

# Test = Code(key="F", easing=1, timing=[1234, 12355], data="0, 1")
# print(Test.getList())
# print(Test)
# print(Test.getString())

Red = [255, 0, 0]
White = [255, 255, 255]

mov = Move(123, [123, 345])
mov2 = Move([451, 471], [310, 231, 361, 142])
mov3 = Move(1, [123, 324, 234, 234])
color = Color(['1:02:323', '2:53:23'], [Red, White])
# print(color)

obj = Object('star.png')
obj.add(mov)
obj.add(mov)
obj.start_loop(12, 34)
obj.add(mov2)
obj.end_loop()

obj.add(color)
obj.add(mov3)

obj.start_loop(4132, 3454)
obj.add(color)
obj.end_loop()

Obj = Object('star.png')
Obj.add(Move(['0:1:2', '1:2:3'], [320, 240, 320, 360]))
Obj.add(Fade([12345, 67890], [1, 0], easing=1))
Obj.print_obj()

obj2 = copy.deepcopy(Obj)

comp = Composition()
comp.add_object(Obj)
comp.add_object(obj2)
comp.print_all()

comp2 = comp.clone()
comp2.set_timing_offset(123)
comp2.set_position_offset(100)
comp2.apply_change()
comp2.print_all()


