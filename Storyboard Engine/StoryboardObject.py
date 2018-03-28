from funcy import flatten

codeArgNum = {
    'M': 2, 'F': 1, 'S': 1,
    'V': 2, 'MX': 1, 'MY': 1,
    'VX': 1, 'VY': 1, 'R': 1,
    'C': 3, 'P': 1
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
        # self.codes.append(','.join(
        # [self.type, self.placement, self.alignment, self.filename, str(self.x), str(self.y)]))

    def add(self, x):
        # if X is a Code
        if isinstance(x, Code):
            self.codes.append(x)
        # if X is a list of Codes
        if isinstance(x, list):
            self.codes.extend(x)

    def start_trigger(self, condition, start_t, end_t):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'T'
        self.codes.append(command(c, condition, start_t, end_t))
        self.currentLoopLevel += 1

    def start_loop(self, start_t, loop_count):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'L'
        self.codes.append(command(c, start_t, loop_count))
        self.currentLoopLevel += 1

    # def add(self, s):
    #     self.codes.append(s)

    def print_obj(self):
        self.codes.insert(0, ','.join(
            [self.type, self.placement, self.alignment, self.fileName, str(self.x), str(self.y)]))
        for code in self.codes:
            print(code)


class Code(Object):
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


class Scene:
    # unFinish
    def __init__(self, timing_offset=0, position_offset=0):
        self.list = []
        self.timingOffset = timing_offset
        self.positionOffset = position_offset

    def add_object(self, *args):
        for arg in args:
            self.list.append(arg)

    def set_timing_offset(self, ms):
        self.timingOffset = ms

    def set_position_offset(self, vector):
        self.positionOffset = vector

    def apply_change(self):
        conut = 0
        for obj in self.list:
            obj.timing[0] = obj.timing[0] + self.timingOffset
            if obj.timing[1] != None:
                obj.timing[1] = obj.timing[1] + self.timingOffset


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
mov2 = Move([12, 34], [1, 2, 1, 2])
mov3 = Move(1, [123, 324, 234, 234])
color = Color(['1:02:323', '2:53:23'], [Red, White])
print(color)

Obj = Object('star.png')
Obj.add(Move(['0:1:2', '1:2:3'], [320, 240, 320, 360]))

Obj.add(Fade([12345, 67890], [1, 0], easing=1))
Obj.print_obj()
