from tools.utils import *

code_arg_num = {
    'M': 2, 'F': 1, 'S': 1,
    'V': 2, 'MX': 1, 'MY': 1,
    'VX': 1, 'VY': 1, 'R': 1,
    'C': 3, 'P': 1
}


class Code:
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

    def __init__(self, key, timing, data, easing=0, loop_level=0):
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
            self.loop_level = loop_level
            return
        # Do format check
        data = array_to_list(data)
        if key not in code_arg_num:
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
        if len(data) % code_arg_num[self.key] == 0:
            if len(data) / code_arg_num[self.key] == 2:
                data1 = data[:code_arg_num[self.key]]
                data2 = data[code_arg_num[self.key]:]
                if data1 == data2:
                    data = data1
            self.data = data
        else:
            raise RuntimeError('Command data set wrongly, please recheck your code.')
        self.loop_level = loop_level

    def set_loop_level(self, loop_level):
        self.loop_level = loop_level

    def get_list(self):
        """Return a list look like [key, easing, start_t, end_t, *data]"""
        if self.key == 'L':
            return array_to_list([self.key, self.timing, self.data])
        if self.key == 'T':
            return array_to_list([self.key, self.data, self.timing])
        for i in range(len(self.data)):
            if isinstance(self.data[i], float):
                self.data[i] = str('%.3f' % self.data[i])
                if self.data[i].split('.')[1] == '000':
                    self.data[i] = self.data[i].split('.')[0]
        return array_to_list([self.key, self.easing, self.timing, self.data])

    def get_string(self):
        """Return a string look like \' M,0,123,456,123,345 \'"""
        return (self.loop_level+1) * ' ' + ','.join(map(str, self.get_list()))

    def __str__(self):
        return self.get_string()

    __repr__ = __str__


class Move(Code):
    def __init__(self, timing, data, easing=0, loop_level=0):
        Code.__init__(self, 'M', timing, data, easing, loop_level)


class MoveX(Code):
    def __init__(self, timing, data, easing=0, loop_level=0):
        Code.__init__(self, 'MX', timing, data, easing, loop_level)


class MoveY(Code):
    def __init__(self, timing, data, easing=0, loop_level=0):
        Code.__init__(self, 'MY', timing, data, easing, loop_level)


class Fade(Code):
    def __init__(self, timing, data, easing=0, loop_level=0):
        Code.__init__(self, 'F', timing, data, easing, loop_level)


class Scale(Code):
    def __init__(self, timing, data, easing=0, loop_level=0):
        Code.__init__(self, 'S', timing, data, easing, loop_level)


class Vector(Code):
    def __init__(self, timing, data, easing=0, loop_level=0):
        Code.__init__(self, 'V', timing, data, easing, loop_level)


class VectorX(Code):
    def __init__(self, timing, data, easing=0, loop_level=0):
        Code.__init__(self, 'VX', timing, data, easing, loop_level)


class VectorY(Code):
    def __init__(self, timing, data, easing=0, loop_level=0):
        Code.__init__(self, 'VY', timing, data, easing, loop_level)


class Rotate(Code):
    def __init__(self, timing, data, easing=0, loop_level=0):
        Code.__init__(self, 'R', timing, data, easing, loop_level)


class Color(Code):
    def __init__(self, timing, data, easing=0, loop_level=0):
        Code.__init__(self, 'C', timing, data, easing, loop_level)


class Loop(Code):
    def __init__(self, timing, loop_count, loop_level=0):
        Code.__init__(self, 'L', timing, data=loop_count, loop_level=loop_level)


class Trigger(Code):
    def __init__(self, timing, trigger_type, loop_level=0):
        Code.__init__(self, 'T', timing, data=trigger_type, loop_level=loop_level)


class Parameter(Code):
    def __init__(self, timing, data, easing=0, loop_level=0):
        Code.__init__(self, 'P', timing, data, easing, loop_level)
