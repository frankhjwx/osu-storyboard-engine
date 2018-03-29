from funcy import flatten
import copy
from utils import time_parser
from utils import get_timing

codeArgNum = {
    'M': 2, 'F': 1, 'S': 1,
    'V': 2, 'MX': 1, 'MY': 1,
    'VX': 1, 'VY': 1, 'R': 1,
    'C': 3, 'P': 1
}


class Code:
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
                return int(ts[0])
            elif len(ts) == 3:
                return time_parser(t)
            else:
                raise RuntimeError('Wrong Timing Format.')
        else:
            return int(t)

    def __init__(self, key, timing, data, easing=0, loop_level=1):
        """Init must take keyword, timing(If it's dict, please write like {\"start_t\": [value], \"end_t\": [value]}. \
        If it's list, please keep two values), data. If you need, write down easing = [value] to change easing value."""
        # if it's Trigger or Loop
        if key == 'T' or key == 'L':
            # L: L,start_t,data(loopCount)
            # T: T,data(triggerType),start_t,end_t
            if key == 'L':
                self.data = int(data)
                if isinstance(timing, tuple):
                    timing = list(timing)
                if isinstance(timing, list):
                    if len(timing) == 0 or len(timing) > 1:
                        raise RuntimeError('Not supported timing argument.')
                    else:
                        self.timing = get_timing(timing[0])
                elif isinstance(timing, dict):
                    if not ('start_t' in timing):
                        raise RuntimeError('Not supported timing argument.')
                    self.timing = timing['start_t']
                else:
                    self.timing = get_timing(timing)
                self.timing = self.normalize_timing_format(self.timing[0])
            if key == 'T':
                self.data = data
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
            self.key = key
            self.loopLevel = loop_level
            return
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

    def set_loop_level(self, loop_level):
        self.loopLevel = loop_level

    def get_list(self):
        """Return a list look like [key, easing, start_t, end_t, *data]"""
        if self.key == 'L':
            return flatten([self.key, self.timing, self.data])
        if self.key == 'T':
            return flatten([self.key, self.data, self.timing])
        return flatten([self.key, self.easing, self.timing, self.data])

    def get_string(self):
        """Return a string look like \' M,0,123,456,123,345 \'"""
        return self.loopLevel * ' ' + ','.join(map(str, self.get_list()))

    def __str__(self):
        return self.get_string()

    __repr__ = __str__


class Move(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'M', timing, data, easing)


class MoveX(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'MX', timing, data, easing)


class MoveY(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'MY', timing, data, easing)


class Fade(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'F', timing, data, easing)


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
        Code.__init__(self, 'R', timing, data, easing)


class Color(Code):
    def __init__(self, timing, data, easing=0):
        Code.__init__(self, 'C', timing, data, easing)


class Loop(Code):
    def __init__(self, timing, loopcount):
        Code.__init__(self, 'L', timing, data=loopcount)


class Trigger(Code):
    def __init__(self, timing, triggerType):
        Code.__init__(self, 'T', timing, data=triggerType)
