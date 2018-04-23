from Storyboard.StoryboardManager import *
from tools.LyricsParser import *
from Storyboard.Camera2D import *

def Scene1():
    s = Scene()
    t = Object('SB/taiji.png')
    t.Move(1000, 2400, 320, 240)
    t.Scale(0.2)
    s.append(t)

    t = Object('SB/taiji.png')
    t.Move(1000, 2400, 200, 240)
    t.Scale(0.2)
    s.append(t)

    t = Object('SB/taiji.png')
    t.Move(1000, 2400, 440, 240)
    t.Scale(0.2)
    s.append(t)

    t = Object('SB/taiji.png')
    t.Move(1000, 2400, 320, 240)
    t.Scale(0.2)
    s.append(t)

    t = Object('SB/taiji.png')
    t.Move(1000, 2400, 320, 120)
    t.Scale(0.2)
    s.append(t)

    t = Object('SB/taiji.png')
    t.Move(1000, 2400, 320, 360)
    t.Scale(0.2)
    s.append(t)
    return s

SBManager = StoryboardManager('F:\osu!\Songs\Efude to kibou no uta', '123.osb')
camera = Camera2D()
camera.Move(1000, 2400, 320, 240, 100, 100)
camera.Rotate(2, 1000, 2400, 0, math.pi)
camera.Scale(2, 1000, 2400, 1, 5)
s = Scene1()
s.set_camera(camera)
SBManager.append_scene(s, cmd_window=True)
SBManager.generate_storyboard(diff_specific=False)
