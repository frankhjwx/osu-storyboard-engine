def Command(*args):
    s = ','.join(str(arg) for arg in args)
    return s


class Object():
    def __init__(self, filename, alignment='Centre', x=320, y=240):
        self.type = 'Sprite'
        self.placement = 'Foreground'
        self.alignment = alignment
        self.filename = filename
        self.x = x
        self.y = y
        self.currentLoopLevel = 1
        self.codes = []
        # self.codes.append(','.join([self.type, self.placement, self.alignment, self.filename, str(self.x), str(self.y)]))

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

    def addT(self, condition, start_t, end_t):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'T'
        self.codes.append(Command(c, condition, start_t, end_t))
        self.currentLoopLevel += 1

    def addL(self, start_t, loopcount):
        spaces = ' ' * self.currentLoopLevel
        c = spaces + 'L'
        self.codes.append(Command(c, start_t, loopcount))
        self.currentLoopLevel += 1

    def add(self, s):
        self.codes.append(s)


    def printObj(self):
        for code in self.codes:
            print(code)

# Usage
# Declare a new Object
Obj = Object('exampleFile.png')
# addM args: easing, start_t, (end_t), start_x, start_y, (end_x), (end_y)
Obj.addM(0, 1234, 1235, 0, 0, 320, 240)
# addT args: condition, start_t, end_t
# WARNING: When using addT and addL operations, looplevel will +1 by default,
# to exit the loop, you should use LoopOut Command
Obj.addT('Hitsound', 2000, 2018)
Obj.addF(0, 0, 500, 0, 1)
Obj.addF(0, 1000, 1500, 1, 0)
Obj.LoopOut()
Obj.addP(0, 1200, 'A')
Obj.addC(0, 1000, 255, 255, 255)

Obj.printObj()