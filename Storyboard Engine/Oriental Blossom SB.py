# This is a Storyboard for https://osu.ppy.sh/beatmapsets/747823/, check it for the visualization!

from Storyboard.StoryboardManager import *
from tools.LyricsParser import *
import random
import math


# Dialogue: 0,0:01:50.37,0:01:55.98,Default,,0,0,0,,{\k561}Eisyo-kobu
# Dialogue: 0,0:01:50.37,0:01:55.98,Default,,0,0,0,,{\k561}Oriental Blossom
# Dialogue: 0,0:01:50.37,0:01:55.98,Default,,0,0,0,,{\k561}Beatmap by
# Dialogue: 0,0:01:50.37,0:01:55.98,Default,,0,0,0,,{\k561}Spectator
# Dialogue: 0,0:01:50.37,0:01:55.98,Default,,0,0,0,,{\k561}Sinnoh
# Dialogue: 0,0:01:50.37,0:01:55.98,Default,,0,0,0,,{\k561}Ascendance
# Dialogue: 0,0:01:50.37,0:01:55.98,Default,,0,0,0,,{\k561}Yumeno Himiko
# Dialogue: 0,0:01:50.37,0:01:55.98,Default,,0,0,0,,{\k561}-Plus-
# Dialogue: 0,0:01:50.37,0:01:55.98,Default,,0,0,0,,{\k561}Razor Sharp
# Dialogue: 0,0:01:50.37,0:01:55.98,Default,,0,0,0,,{\k561}Storyboard by

# math.pi also works
pi = 3.1415926
song_folder = 'F:/osu!/Songs/747823 Eisyo-kobu - Oriental Blossom'
sb_filename = 'Eisyo-kobu - Oriental Blossom (Spectator).osb'
difftoMapper = {
    'Cup': 3, 'Salad': 3, 'Platter': 3, 'Rain': 3, 'Oriental': 3,
    "Himiko's Rain": 6, "Plus's Overdose": 7, "Sinnoh's Overdose": 4,
    "Ascendance's Overdose": 5, "Razor's Overdose": 8
}
# text spacing
spacing = 0


def Background():
    objs = []

    bg2 = Object('SB/background.jpg')
    bg2.Loop(0, time_parser('01:56:673')/3000+1)
    bg2.Move(0, 3000, 320 + 28, 240, 320 - 28, 240)
    bg2.LoopOut()

    objs.append(bg2)
    #objs.append(bg3)

    return Scene(objs)

def BGBlossoms():
    blossom = []

    blossom1 = Object('SB/cherry blossom.png', x=78, y=180)
    blossom1.Color(0, [255, 190, 190])
    blossom1.Fade(674, 1007, 0, 0.8)
    blossom1.Fade(1007, 10007, 0.8)
    blossom1.Rotate(674, 10007, 0, pi * 0.4)
    blossom.append(blossom1)

    blossom2 = Object('SB/cherry blossom.png', x=388, y=340)
    blossom2.Color(0, [255, 190, 190])
    blossom2.Fade(674, 1007, 0, 0.8)
    blossom2.Fade(1007, 10007, 0.8)
    blossom2.Rotate(674, 10007, pi * 0.1, - pi * 0.3)
    blossom.append(blossom2)

    blossom3 = Object('SB/cherry blossom.png', x=562, y=240)
    blossom3.Color(0, [255, 190, 190])
    blossom3.Fade(674, 1007, 0, 0.8)
    blossom3.Fade(1007, 10007, 0.8)
    blossom3.Scale(674, 0.8)
    blossom3.Rotate(674, 10007, pi * 0.7, pi)
    blossom.append(blossom3)

    return Scene(blossom)

def topCover():
    objs = []
    Pink = [236, 197, 183]
    pinkBar1 = Object('SB/dot.png', origin='TopCentre', x=320, y=0)
    pinkBar1.Vector(0, '01:56:673', 854, 100)
    pinkBar1.Color(0, Pink)

    pinkBar2 = Object('SB/dot.png', origin='BottomCentre', x=320, y=480)
    pinkBar2.Vector(0, '01:56:673', 854, 100)
    pinkBar2.Color(0, Pink)
    objs.append(pinkBar1)
    objs.append(pinkBar2)
    return Scene(objs)

def topCoverPatterns():
    objs = Scene()
    for i in range(0, 125, 25):
        for j in range(-107 - 25 * (int(i / 25) % 2) - 25, 854 - 75, 50):
            if i != 100:
                element = Object('SB/e1.png', x=j, y=i)
                element.Color(0, '01:56:673', [255, 230, 230])
                element.Fade(0, 0.5)
                element.Loop(0, time_parser('01:56:673') / 6000 + 1)
                element.Move(0, 6000, j, i, j + 50, i)
                element.LoopOut()
                objs.append(element)
            else:
                element = Object('SB/e2.png', origin='BottomCentre', x=j, y=i)
                element.Color(0, '01:56:673', [255, 230, 230])
                element.Fade(0, 0.5)
                element.Loop(0, time_parser('01:56:673') / 6000 + 1)
                element.Move(0, 6000, j, i, j + 50, i)
                element.LoopOut()
                objs.append(element)

    for i in range(380, 481, 25):
        for j in range(-107 - 25 * (int(i / 25) % 2) - 25, 854 - 75, 50):
            if i != 380:
                element = Object('SB/e1.png', x=j, y=i)
                element.Color(0, '01:56:673', [255, 230, 230])
                element.Fade(0, 0.5)
                element.Loop(0, time_parser('01:56:673') / 6000 + 1)
                element.Move(0, 6000, j, i, j + 50, i)
                element.LoopOut()
                objs.append(element)
            else:
                element = Object('SB/e3.png', origin='TopCentre', x=j, y=i)
                element.Color(0, '01:56:673', [255, 230, 230])
                element.Fade(0, 0.5)
                element.Loop(0, time_parser('01:56:673') / 6000 + 1)
                element.Move(0, 6000, j, i, j + 50, i)
                element.LoopOut()
                objs.append(element)
    return objs

def moveDoor():
    objs = []
    t = [9173, 9673, 10007]
    t_end = 11007
    door1 = Object('SB/door.jpg', origin='CentreLeft', x=320, y=240)
    door1.MoveX(1, t[2] - 333, t[2], -107 - 150 + 277, -107 + 277)
    door1.MoveX(t_end, t_end + 150, -107 + 277, -107 - 150)
    objs.append(door1)

    door1 = Object('SB/door.jpg', origin='CentreLeft', x=320, y=240)
    door1.MoveX(1, t[1] - 333, t[1], -107 - 150 + 147, -107 + 147)
    door1.MoveX(t_end, t_end + 150, -107 + 147, -107 - 150)
    objs.append(door1)

    door1 = Object('SB/door.jpg', origin='CentreLeft', x=320, y=240)
    door1.MoveX(1, t[0]-333, t[0], -107 - 150, -107)
    door1.MoveX(t_end, t_end + 150, -107, -107 - 150)
    objs.append(door1)

    door2 = Object('SB/door.jpg', origin='CentreRight', x=320, y=240)
    door2.MoveX(1, t[2] - 333, t[2], 747 + 150 - 277, 747 - 277)
    door2.MoveX(t_end, t_end + 150, 747 - 277, 747 + 150)
    objs.append(door2)

    door2 = Object('SB/door.jpg', origin='CentreRight', x=320, y=240)
    door2.MoveX(1, t[1] - 333, t[1], 747 + 150 - 147, 747 - 147)
    door2.MoveX(t_end, t_end + 150, 747 - 147, 747 + 150)
    objs.append(door2)

    door2 = Object('SB/door.jpg', origin='CentreRight', x=320, y=240)
    door2.MoveX(1, t[0] - 333, t[0], 747 + 150, 747)
    door2.MoveX(t_end, t_end + 150, 747, 747 + 150)
    objs.append(door2)
    return Scene(objs)

def Scene1():
    objs = []
    yama = Object('SB/yama.png', x=129, y=303)
    yama.Fade(11340, 12007, 0, 1)
    yama.Fade(12007, 1)
    yama.Fade(21673, 0)
    yama.Scale(11340, 0.8)
    objs.append(yama)

    sun = Object('SB/sun.png', x=570, y=150)
    sun.Fade(11340, 12007, 0, 1)
    sun.Fade(12007, 1)
    sun.Fade(21673, 0)
    sun.Scale(11340, 0.25)
    for i in range(8):
        cloud = Object('SB/cloud'+str(random.randint(1,3))+'.png', x=320, y=random.randint(150, 220))
        cloud.MoveX(11340, 32673, 150*i, 150*i - 400)
        cloud.Fade(11340, 12007, 0, 0.6)
        cloud.Parameter(11340, 'H')
        cloud.Color(11340, [255, 180, 180])
        cloud.Scale(11340, 0.5)
        cloud.Fade(21673, 0)
        objs.append(cloud)
    objs.append(sun)

    timings = ['00:20:673', '00:21:007', '00:21:340']
    white1 = Object('SB/dot.png', origin='CentreLeft', x=-107, y=240)
    white1.Vector(time_parser(timings[0]) - 100, time_parser(timings[0]) + 100, 0, 280, 854, 280)
    white1.Fade(timings[0],  time_parser(timings[2]) + 100, 0.3333)

    white2 = Object('SB/dot.png', origin='CentreRight', x=747, y=240)
    white2.Vector(time_parser(timings[1]) - 100, time_parser(timings[1]) + 100, 0, 280, 854, 280)
    white2.Fade(timings[1],  time_parser(timings[2]) + 100, 0.6666)

    white3 = Object('SB/dot.png', origin='CentreLeft', x=-107, y=240)
    white3.Vector(time_parser(timings[2]) - 100, time_parser(timings[2]) + 100, 0, 280, 854, 280)
    white3.Fade(timings[2], '00:21:673', 1)

    objs.append(white1)
    objs.append(white2)
    objs.append(white3)

    for i in range(40):
        for j in range(14):
            x = 854/40*i - 107
            y = 280/14*j + 100
            start_t = time_parser('00:21:673') + j * 20
            square = Object('SB/dot.png', origin='TopLeft')
            square.Vector('00:21:673', 854/40, 280/14)
            square.Move(start_t, start_t + 200, x, y, x, y + 10)
            square.Rotate(start_t, start_t + 200, 0, pi * 0.2)
            square.Fade(start_t, start_t + 200, 1, 0)
            objs.append(square)

    return Scene(objs)

def Scene2():
    objs = Scene()
    Rotate_Center = [320, 240]
    R = 200
    taiji = Object('SB/taiji.png')
    taiji.Fade(22007, 22340, 0, 1)
    taiji.Rotate(22007, 32673, 0, 0.1 * pi)
    taiji.Scale(22007, 0.4)

    koi1 = Object('SB/koi.png')
    koi1.MoveX(22007, 32673, 320 + R, 320 + math.cos(0.1*pi)*R)
    koi1.MoveY(22007, 32673, 240, 240 - math.sin(0.1*pi)*R)
    koi1.Rotate(22007, 32673, 0, -0.1 * pi)
    koi1.Parameter(22007, 'H')
    koi1.Scale(22007, 0.2)
    koi1.Fade(22007, 22340, 0, 1)

    koi2 = Object('SB/koi.png')
    koi2.MoveX(22007, 32673, 320 - R, 320 - math.cos(0.1 * pi) * R)
    koi2.MoveY(22007, 32673, 240, 240 + math.sin(0.1 * pi) * R)
    koi2.Rotate(22007, 32673, 0, -0.1 * pi)
    koi2.Parameter(22007, 'V')
    koi2.Scale(22007, 0.2)
    koi2.Fade(22007, 22340, 0, 1)

    objs.append(taiji)
    objs.append(koi1)
    objs.append(koi2)

    white1 = Object('SB/dot.png', origin='CentreLeft', x=-107, y=240)
    white1.Vector(2, '00:32:007', '00:32:673', 0, 280, 427, 280)
    white1.Fade('00:32:673', '00:33:007', 1, 0)

    white2 = Object('SB/dot.png', origin='CentreRight', x=747, y=240)
    white2.Vector(2, '00:32:007', '00:32:673', 0, 280, 427, 280)
    white2.Fade('00:32:673', '00:33:007', 1, 0)

    objs.append(white1)
    objs.append(white2)

    return objs

def Scene3():
    objs = Scene()
    e4 = Object('SB/e4.png')
    e4.Move(32673, 43340, 550, 300, 530, 300)
    e4.Scale(32673, 0.9)

    e5 = Object('SB/e5.png')
    e5.Move(32673, 43340, 150, 200, 170, 200)
    e5.Scale(32673, 0.6)
    e5.Rotate(32673, pi*0.1)

    objs.append(e4)
    objs.append(e5)

    return objs

def Scene4():
    objs = Scene()
    sakurabranch = Object('SB/sakura branch.png', origin='CentreLeft', x=-107, y=240)
    sakurabranch.Scale(43340, 54007, 0.45)

    boat = Object('SB/boat.png')
    boat.Move(43340, 54007, 500, 225, 460, 240)
    boat.Scale(43340, 0.5)

    pavilion = Object('SB/pavilion.png', x=364, y=175)
    pavilion.Fade(43340, 0.75)
    pavilion.Scale(43340, 54007, 0.2)
    objs.append(sakurabranch)
    objs.append(boat)
    #objs.append(pavilion)

    # 转5圈 每圈36个
    start_t = 42007
    end_t = 43340
    pos_x = 107
    pos_y = 240
    r = 250
    r_current = 0
    rad_current = 0
    for i in range(36 * 5):
        t = int((end_t - start_t) / (36 * 5) * i + start_t)
        x = pos_x + r_current * math.cos(rad_current)
        y = pos_y + r_current * math.sin(rad_current)
        selfR = random.random() * pi
        sakura = Object('SB/c.png')
        sakura.Scale(t - 100, t, 0, 0.2)
        sakura.Move(t - 100, t + 500, x, y, x + random.randint(-5, 5), y + random.randint(-5, 5))
        sakura.Rotate(t - 100, t + 500, selfR, selfR + pi * 0.5)
        sakura.Fade(end_t, end_t + 200, 1, 0)
        r_current += r / (36 * 5)
        rad_current += pi / 18
        objs.append(sakura)

    pos_x = 747 - int(854/4)
    r_current = 0
    rad_current = 0
    for i in range(36 * 5):
        t = int((end_t - start_t) / (36 * 5) * i + start_t)
        x = pos_x + r_current * math.cos(rad_current)
        y = pos_y + r_current * math.sin(rad_current)
        selfR = random.random() * pi
        sakura = Object('SB/c.png')
        sakura.Scale(t - 100, t, 0, 0.2)
        sakura.Move(t - 100, t + 500, x, y, x + random.randint(-5, 5), y + random.randint(-5, 5))
        sakura.Rotate(t - 100, t + 500, selfR, selfR + pi * 0.5)
        sakura.Fade(end_t, end_t + 200, 1, 0)
        r_current += r / (36 * 5)
        rad_current -= pi / 18
        objs.append(sakura)

    return objs

def Scene5():
    objs = Scene()
    bamboo = Object('SB/bamboo.png')
    bamboo.Fade(54007, 54673, 0, 1)
    bamboo.Scale(54007, 0.28)
    bamboo.Rotate(54007, -0.2)
    bamboo.Move(54007, 66007, 120, 240, 100, 240)
    bamboo.Fade(65673, 66007, 1, 0)
    objs.append(bamboo)

    butterfly1 = Object('SB/butterfly.png')
    butterfly1.Scale(54007, 0.8)
    butterfly1.Move(54007, 66007, 508, 207, 514, 196)
    butterfly1.Fade(65673, 66007, 1, 0)

    butterfly2 = Object('SB/butterfly.png')
    butterfly2.Scale(54007, 0.6)
    butterfly2.Rotate(54007, -0.54)
    butterfly2.Move(54007, 66007, 341, 281, 334, 259)
    butterfly2.Fade(65673, 66007, 1, 0)

    objs.append(butterfly1)
    objs.append(butterfly2)

    for i in range(40):
        for j in range(14):
            x = 854/40*i - 107
            y = 280/14*j + 100
            start_t = 53340 + j * 35
            square = Object('SB/dot.png', origin='TopLeft')
            square.Vector('00:21:673', 854/40, 280/14)
            square.Move(start_t, start_t + 200, x, y + 10, x, y)
            square.Rotate(start_t, start_t + 200, pi * 0.2, 0)
            square.Fade(start_t, start_t + 200, 0, 1)
            square.Fade(54007, 54673, 1, 0)
            objs.append(square)

    return objs

def Scene6():
    objs = Scene()
    Rotate_Center = [320, 240]
    R = 200
    taiji = Object('SB/taiji_pink.png')
    taiji.Fade(88673, 89340, 0, 1)
    taiji.Rotate(88673, 110007, 0, 0.2 * pi)
    taiji.Scale(88673, 0.4)

    koi1 = Object('SB/koi_pink.png')
    koi1.MoveX(88673, 110007, 320 + R, 320 + math.cos(0.2 * pi) * R)
    koi1.MoveY(88673, 110007, 240, 240 - math.sin(0.2 * pi) * R)
    koi1.Rotate(88673, 110007, 0, -0.2 * pi)
    koi1.Parameter(88673, 'H')
    koi1.Scale(88673, 0.2)
    koi1.Fade(88673, 89340, 0, 1)

    koi2 = Object('SB/koi_pink.png')
    koi2.MoveX(88673, 110007, 320 - R, 320 - math.cos(0.2 * pi) * R)
    koi2.MoveY(88673, 110007, 240, 240 + math.sin(0.2 * pi) * R)
    koi2.Rotate(88673, 110007, 0, -0.2 * pi)
    koi2.Parameter(88673, 'V')
    koi2.Scale(88673, 0.2)
    koi2.Fade(88673, 89340, 0, 1)

    # sakura cycle
    R = 300
    for i in range(240):
        sakura = Object('SB/sakura.png')
        start_t = 88673 - 30000 + random.randint(0, 30000)
        r = R + random.randint(-20, 20)
        posx = [427 - r - 107, 427 - 107, 427 + r - 107, 427 - 107]
        posy = [240, 240 + r, 240, 240 - r]
        t = []
        for i in range(8):
            t.append(start_t + i * 30000/4)
        for i in range(7):
            sakura.MoveX(2 - i%2, t[i], t[i+1], posx[i%4], posx[(i+1)%4])
            sakura.MoveY(1 + i%2, t[i], t[i+1], posy[i%4], posy[(i+1)%4])
        sakura.Fade(88673, 88674, 0, 1)
        start_rad = 2*pi*random.random()
        sakura.Rotate(start_t, start_t + 30000*2, start_rad, start_rad + pi * 2)
        sakura.Scale(start_t, random.randint(20, 60)/100)
        sakura.Fade(110007, 0)
        objs.append(sakura)

    objs.append(taiji)
    objs.append(koi1)
    objs.append(koi2)

    start_t = 108673
    end_t = 110007
    pos_x = 107
    pos_y = 150
    r = 300
    r_current = 0
    rad_current = 0
    for i in range(36 * 5):
        t = int((end_t - start_t) / (36 * 5) * i + start_t)
        x = pos_x + r_current * math.cos(rad_current)
        y = pos_y + r_current * math.sin(rad_current)
        selfR = random.random() * pi
        sakura = Object('SB/c.png')
        sakura.Scale(t - 100, t, 0, 0.35)
        sakura.Move(t - 100, t + 500, x, y, x + random.randint(-5, 5), y + random.randint(-5, 5))
        sakura.Rotate(t - 100, t + 500, selfR, selfR + pi * 0.5)
        sakura.Fade(end_t, end_t + 1, 1, 0)
        r_current += r / (36 * 5)
        rad_current += pi / 18
        objs.append(sakura)

    pos_x = 747 - int(854 / 4)
    pos_y = 330
    r_current = 0
    rad_current = 0
    for i in range(36 * 5):
        t = int((end_t - start_t) / (36 * 5) * i + start_t)
        x = pos_x + r_current * math.cos(rad_current)
        y = pos_y + r_current * math.sin(rad_current)
        selfR = random.random() * pi
        sakura = Object('SB/c.png')
        sakura.Scale(t - 100, t, 0, 0.35)
        sakura.Move(t - 100, t + 500, x, y, x + random.randint(-5, 5), y + random.randint(-5, 5))
        sakura.Rotate(t - 100, t + 500, selfR, selfR + pi * 0.5)
        sakura.Fade(end_t, end_t+1, 1, 0)
        r_current += r / (36 * 5)
        rad_current -= pi / 18
        objs.append(sakura)

    return objs

def generateSakura(start_t, end_t, pos_x, pos_y):
    sakura = Object('SB/sakura.png')
    x = pos_x
    y = pos_y
    scale = random.randint(10, 40) / 100
    xspeed = random.randint(5, 7)/200 / scale
    yspeed = random.randint(2, 4)/400 / scale
    duration = (400 - y)/yspeed
    sakura.Move(start_t, start_t + duration, x, y, x + xspeed*duration, y + yspeed*duration)
    sakura.Scale(start_t, scale)
    sakura.Fade(start_t, start_t+500, 0, 1)
    sakura.Rotate(start_t, start_t + duration, random.random() * pi * 2, random.random() * pi * 4 + pi * 2)
    if start_t + duration > 88673:
        sakura.Fade(88672, 88673, 1, 0)
    return sakura

def SakuraEffect():
    objs = Scene()
    for i in range(300):
        objs.append(generateSakura(random.randint(67340, 87340), 88673, random.randint(-36, 216), random.randint(200, 307)))
    return objs

def Torli(timing, cx, cy):
    start_t = timing - 200
    end_t = timing + 200
    torli = Object('SB/torli.png')
    torli.Move(9, start_t, end_t, cx, cy, 425, 300)
    torli.Scale(9, start_t, end_t, 0.05, 2)
    torli.Rotate(5, 87140, 88888, -0.1, 0.05)
    torli.Fade(start_t, start_t + 300, 0, 1)
    torli.Fade(end_t, 0)
    return torli

def CrossTorli():
    objs = Scene()
    bg = Object('SB/bg-pink.png')
    bg.Fade(87007, 87340, 0, 1)
    bg.Fade(88673, 89007, 1, 0)
    objs.append(bg)
    # 150, 175
    timings = [87340, 87590, 87840]
    for t in timings:
        objs.append(Torli(t, 150 + (t-87340)/20, 175))
    for i in range(8):
        objs.append(Torli(88007 + i*83, 150 + (88007 + i*83-87340)/20, 175))
    return objs

def RayEffect(timing, fade):
    Ray = Object('SB/ray.png', origin='CentreLeft')
    Ray.Scale(timing - 100, timing + 100, 0, 1)
    Ray.Rotate(timing, random.random()*2*pi)
    Ray.Color(timing, [255, 120, 120])
    Ray.Fade(timing, timing + 400, fade ,0)
    return Ray

def Ending():
    objs = Scene()
    w = Object('SB/dot.png')
    w.Vector(110007, 110673, 854, 480)
    w.Fade(110007, 110673, 1, 0)
    objs.append(w)

    for i in range(30):
        objs.append(RayEffect(110340 + i*167, 0.5/35*(35-i)))
    return objs

def EndingBlack():
    objs = Scene()
    w = Object('SB/dot.png')
    w.Vector(115173, 116007, 854, 480)
    w.Fade(115173, 116007, 0, 1)
    w.Color(115173, 116007, [0,0,0])
    objs.append(w)
    return objs


def FanEffect():
    objs = Scene()
    bg = Object('SB/bg-pink.png')
    bg.Fade(36340, 36673, 0, 1)
    bg.Fade(38007, 38340, 1, 0)
    objs.append(bg)
    t0 = 36673
    for i in range(8):
        start_t = t0 + 167 * i
        x0 = -107 + 854 / 4 * (i % 4) + 854 / 4 / 2
        y0 = 0 + 480 / 2 * int(i / 4) + 480 / 2 / 2
        scale = 1 / 4
        fan = Object('SB/fan.png')
        fan.Move(start_t, start_t + 100, x0 - 5 * scale, y0 - 5 * scale, x0, y0)
        fan.Rotate(start_t, start_t + 100, -0.1 * pi, 0)
        fan.Scale(start_t, start_t + 167, scale)
        fan.Fade(38007, 38340, 1, 0)
        objs.append(fan)

    return objs

def LanternEffect():
    objs = Scene()
    bg = Object('SB/bg-pink.png')
    bg.Fade(47007, 47340, 0, 1)
    bg.Fade(48673, 49007, 1, 0)
    objs.append(bg)
    t0 = 47340
    for i in range(8):
        start_t = t0 + 167 * i
        x0 = -107 + 854 / 8 * i + 854 / 8 / 2
        y0 = 0 + 480 / 2 / 2
        scale = 1 / 4
        lantern = Object('SB/lantern.png')
        lantern.Move(start_t, start_t + 100, x0 - 5 * scale, y0 - 5 * scale, x0, y0)
        lantern.Rotate(start_t, start_t + 100, 0.1 * pi, 0)
        lantern.Scale(start_t, start_t + 167, scale)
        lantern.Fade(48673, 49007, 1, 0)
        objs.append(lantern)

        x0 = -107 + 854 / 8 * (7 - i) + 854 / 8 / 2
        y0 = 0 + 480 / 2 + 480 / 2 / 2
        lantern = Object('SB/lantern.png')
        lantern.Move(start_t, start_t + 100, x0 - 5 * scale, y0 - 5 * scale, x0, y0)
        lantern.Rotate(start_t, start_t + 100, -0.1 * pi, 0)
        lantern.Scale(start_t, start_t + 167, scale)
        lantern.Fade(48673, 49007, 1, 0)
        objs.append(lantern)

    return objs

def Tree():
    objs = []
    sakuratree = Object('SB/blossom tree.png', x=87, y=262)
    sakuratree.Scale(66673, 0.68)
    sakuratree.Fade(66673, 67673, 0, 1)
    sakuratree.Fade(67673, 87340, 1)
    objs.append(sakuratree)
    return Scene(objs)

def Blossom(start_t, end_t, pos_x, pos_y, r, filename='SB/sakura.png'):
    objs = []
    # 转5圈 每圈36个
    r_current = 0
    rad_current = 0
    for i in range(36*5):
        t = int((end_t-start_t)/(36*5)*i + start_t)
        x = pos_x + r_current * math.cos(rad_current)
        y = pos_y + r_current * math.sin(rad_current)
        selfR = random.random() * pi
        sakura = Object(filename)
        sakura.Scale(t - 100, t + 500, 0, 2.5)
        sakura.Move(t - 100, t + 500, x, y, x + random.randint(-5, 5), y + random.randint(-5, 5))
        sakura.Rotate(t - 100, t + 500, selfR, selfR + pi * 0.5)
        sakura.Fade(t+200, t+500, 1, 0)
        r_current += r / (36*5)
        rad_current += pi / 18
        objs.append(sakura)
    return Scene(objs)


def beginning():
    objs = []
    for i in range(-107, 854, 51):
        for j in range(0, 480, 48):
            end_t = random.randint(474, 674)
            square = Object('SB/dot.png', origin='TopLeft', x=i, y=j)
            square.Vector(0, 51, 48)
            square.Color(0, [0, 0, 0])
            square.Fade(0, end_t - 200, 1)
            square.Fade(end_t - 200, end_t + 100, 1, 0)
            objs.append(square)
    return Scene(objs)

def genLyric(sentence, posx, posy, start_t, end_t, scale=0.6):
    objs = []
    x = posx
    y = posy
    movespeed = 0.005
    for ch in sentence.letters:
        dt = random.randint(-200, 200)
        obj = Object(ch.filename, origin='BottomLeft')
        obj.Move(start_t - 300, end_t + 400, x, y, x + movespeed*(end_t-start_t+700), y)
        obj.Fade(start_t + dt - 100, start_t + dt + 400, 0, 1)
        obj.Fade(end_t + dt - 200, end_t + dt + 200, 1, 0)
        obj.Color(start_t, [0,0,0])
        obj.Scale(start_t, scale)
        x += (ch.width + spacing) * scale
        objs.append(obj)
    return objs

def generateTitle(lp):
    objs = Scene()
    objs.append(genLyric(lp.sentences[0], 100, 220, 110340, 112507))
    objs.append(genLyric(lp.sentences[1], 200, 300, 110340, 112507))
    return objs

def generateDiff(lp, diff_name):
    objs = Scene()
    #print(diffName, difftoMapper[diffName])
    objs.append(genLyric(lp.sentences[2], -50, 180, 112673, 115173))
    objs.append(genLyric(lp.sentences[difftoMapper[diff_name]], 50, 240, 112673, 115173))

    objs.append(genLyric(lp.sentences[9], 300, 280, 112673, 115173))
    objs.append(genLyric(lp.sentences[6], 400, 340, 112673, 115173))
    return objs


# Create StoryboardManager
SBManager = StoryboardManager(song_folder, sb_filename, create_backup=True)

# These backgrounds will be set to invisible in storyboard.
SBManager.set_bg(['himiko.jpg', 'me.jpg', 'ascendance.jpg', 'bg-plus.jpg', 'bg-razor.jpg', 'sino.jpg'])

# Create a CharacterRenderer
CR = CharacterRenderer(font_path='Fonts/LEVIBRUSH.TTF', file_path='SB/letters/')
subtitles = LyricParser(CR)
subtitles.ass_reader('Subtitles\subtitles.ass')
# If Character set already generated before, CR.render() can be omitted
#CR.render()

bg = Background()
bgBlossoms = BGBlossoms()
doors = moveDoor()
s1 = Scene1()
s2 = Scene2()
s3 = Scene3()
s4 = Scene4()
s5 = Scene5()
s6 = Scene6()
tree = Tree()
top = topCover()
topPattern = topCoverPatterns()
beginning = beginning()
blossom = Blossom(66007, 67173, 90, 265, 150)
skr = SakuraEffect()
fans = FanEffect()
lanterns = LanternEffect()
torlis = CrossTorli()
ending = Ending()
endingblack = EndingBlack()

# create subtitles for each diff
title = generateTitle(subtitles)
diff = {}
for diff_name in SBManager.get_diff_names():
    diff[diff_name] = generateDiff(subtitles, diff_name)

bg.Fade(87340, 87341, 1, 0)
bg.Fade(88673, 1)
topPattern.Fade(87340, 87341, 0.5, 0)
topPattern.Fade(88673, 0.5)
top.Fade(87340, 87341, 1, 0)
top.Fade(88673, 1)

bg.Fade(116006, 116007, 1, 0)
top.Fade(116006, 116007, 1, 0)
topPattern.Fade(116006, 116007, 0.5, 0)

SBManager.append_scene(bgBlossoms)
SBManager.append_scene(doors)
SBManager.append_scene(s1)
SBManager.append_scene(s2)
SBManager.append_scene(s3)
SBManager.append_scene(s4)
SBManager.append_scene(s5)
SBManager.append_scene(s6)
SBManager.append_scene(skr)
SBManager.append_scene(tree)
SBManager.append_scene(blossom)
SBManager.append_scene(ending)
SBManager.append_scene(top)
SBManager.append_scene(topPattern)
SBManager.append_scene(beginning)
SBManager.append_scene(torlis)
SBManager.append_scene(endingblack)
SBManager.append_scene(fans)
SBManager.append_scene(lanterns)
SBManager.append_scene(title)

w = Object('SB/dot.png')
w.Fade(64673 - 400, 64673, 0, 0.6)
w.Color([0, 0, 0])
w.Vector(854, 480)
w.Fade(66007 - 400, 66007, 0.6, 0)
scene = Scene([w])
SBManager.append_scene(scene)

for diff_name in SBManager.get_diff_names():
    SBManager.append_scene(bg, diff_name)
    SBManager.append_scene(diff[diff_name], diff_name)

# This can be used to check some commands inside command window.
# These codes won't be generated into storyboard files
# SBManager.append_scene(torlis, cmd_window=True)

SBManager.generate_storyboard(diff_specific=True)
SBManager.delete_backups()