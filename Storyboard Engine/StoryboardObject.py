from funcy import flatten

def Command(*args):
    s = ','.join(str(arg) for arg in args)
    return s

def Timing(start_t, end_t = ''):
    "Return a list like [start_t, end_t], end_t default value is a empty."
    return [start_t, end_t]

class Object():
    def __init__(self, file_name, alignment='Centre', x=320, y=240):
        self.type = 'Sprite'
        self.placement = 'Foreground'
        self.alignment = alignment
        self.file_name = file_name
        self.x = x
        self.y = y
        self.currentLoopLevel = 1
        self.codes = []
        # self.codes.append(','.join(
        # [self.type, self.placement, self.alignment, self.filename, str(self.x), str(self.y)]))

    def LoopOut(self):
        self.currentLoopLevel -= 1

    def addM(self, easing, *args):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'M'
        if len(args) == 6:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 4:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 3:
            self.codes.append(Command(c, easing, args[0], '', args[1], args[2]))

    def addV(self, easing, *args):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'V'
        if len(args) == 6:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 4:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 3:
            self.codes.append(Command(c, easing, args[0], '', args[1], args[2]))

    def addF(self, easing, *args):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'F'
        if len(args) == 4:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 3:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 2:
            self.codes.append(Command(c, easing, args[0], '', args[1]))

    def addR(self, easing, *args):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'R'
        if len(args) == 4:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 3:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 2:
            self.codes.append(Command(c, easing, args[0], '', args[1]))

    def addS(self, easing, *args):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'S'
        if len(args) == 4:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 3:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 2:
            self.codes.append(Command(c, easing, args[0], '', args[1]))

    def addVX(self, easing, *args):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'VX'
        if len(args) == 4:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 3:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 2:
            self.codes.append(Command(c, easing, args[0], '', args[1]))

    def addVY(self, easing, *args):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'VY'
        if len(args) == 4:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 3:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 2:
            self.codes.append(Command(c, easing, args[0], '', args[1]))

    def addMX(self, easing, *args):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'MX'
        if len(args) == 4:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 3:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 2:
            self.codes.append(Command(c, easing, args[0], '', args[1]))

    def addMY(self, easing, *args):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'MY'
        if len(args) == 4:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 3:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 2:
            self.codes.append(Command(c, easing, args[0], '', args[1]))

    def addC(self, easing, *args):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'C'
        if len(args) == 8:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 5:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 4:
            self.codes.append(Command(c, easing, args[0], '', args[1], args[2], args[3]))

    def addP(self, easing, *args):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'P'
        if len(args) == 3:
            self.codes.append(Command(c, easing, *args))
        if len(args) == 2:
            self.codes.append(Command(c, easing, args[0], '', args[1]))

    def startTrigger(self, condition, start_t, end_t):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'T'
        self.codes.append(Command(c, condition, start_t, end_t))
        self.currentLoopLevel += 1

    def startLoop(self, start_t, loop_count):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'L'
        self.codes.append(Command(c, start_t, loop_count))
        self.currentLoopLevel += 1

    def add(self, s):
        self.codes.append(s)


    def printObj(self):
        self.codes.insert(0, ','.join([self.type, self.placement, self.alignment, self.file_name, str(self.x), str(self.y)]))
        for code in self.codes:
            print(code)

class Code(Object):
    def __init__(self, key, timing, data, easing = 0):
        "Init must take keyword, timing(If it's dict, please write like {\"start_t\": [value], \"end_t\": [value]}. If it's list, please keep two values), data. If you need, write down easing = [value] to change easing value."
        self.key = key
        self.easing = easing
        if isinstance(timing, list):
            self.timing = timing
        elif isinstance(timing, dict):
            self.timing = Timing(timing['start_t'], timing['end_t'])
        elif isinstance(timing, tuple):
            self.timing = list(timing)
        else:
            self.timing = Timing(timing)
        self.data = data

    def getList(self):
        "Return a list look like [key, easing, start_t, end_t, *data]"
        return flatten([self.key, self.easing, self.timing, self.data])

    def getString(self):
        "Return a string look like \' M,0,123,456,123,345 \'"
        return ','.join(map(str, self.getList()))

    def __str__(self):
        return self.getString()

    __repr__ = __str__

class Move(Code):
    # unfinish
    def __init__(self, timing, data, easing = 0):
        if isinstance(data, list) and len(data) % 2 == 0:
            Code.__init__(self, 'M', timing, data, easing = easing)
    
class Fade(Code):
    # unfinish
    def __init__(self, timing, data, easing = 0):
        if isinstance(data, list) and len(data) == 2:
            if data[0] == data[1]:
                Code.__init__(self, 'F', timing, data[0], easing = easing)
            else:
                Code.__init__(self, 'F', timing, data, easing = easing)

class Scale(Code):
    # unfinish
    def __init__(self, timing, data, easing = 0):
        if isinstance(data, list):
            Code.__init__(self, 'S', timing, data, easing)


class Rotate(Code):
    # unfinish
    def __init__(self, timing, data, easing = 0):
        if isinstance(data, list):
            Code.__init__(self, 'R', timing, data, easing = easing)

class Scene():
    # unfinish
    def __init__(self, timingOffset = 0, positionOffset = 0):
        self.list = []
        self.timingOffset = timingOffset
        self.positionOffset = positionOffset

    def addObject(self, *args):
        for arg in args:
            self.list.append(arg)

    def setTimingOffset(self, ms):
        self.timingOffset= ms

    def setPositionOffset(self, vector):
        self.positionOffset = vector

    def applyChange():
        conut = 0
        for obj in self.list:
            obj.timing[0] = obj.timing[0] + timingOffset
            if obj.timing[1] != None:
                obj.timing[1] = obj.timing[1] + timingOffset


# Usage
# Declare a new Object
Obj = Object('exampleFile.png')
# addM args: easing, start_t, (end_t), start_x, start_y, (end_x), (end_y)
Obj.addM(0, 1234, 1235, 0, 0, 320, 240)
# addT args: condition, start_t, end_t
# WARNING: When using addT and addL operations, looplevel will +1 by default,
# to exit the loop, you should use LoopOut Command
Obj.startTrigger('Hitsound', 2000, 2018)
Obj.addF(0, 0, 500, 0, 1)
Obj.addF(0, 1000, 1500, 1, 0)
Obj.LoopOut()
Obj.addP(0, 1200, 'A')
Obj.addC(0, 1000, 255, 255, 255)

Obj.printObj()

Test = Code(key = "F", easing = 1, timing = [1234, 12355], data = "0, 1")
print(Test.getList())

print(Test)

print(Test.getString())

m = Move(123,[123,345])
print(m) # M,0,123,,123,345


