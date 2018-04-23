from Storyboard.StoryboardManager import *
from tools.LyricsParser import *
from Storyboard.Camera2D import *

def Scene1():
    s = Scene()
    sakura = Object('sakura.png')
    sakura.Move(1000, 2400, 320, 240, 600, 800)
    sakura.Scale(1000, 2400, 1, 5)
    sakura.Rotate(1000, 2400, 0, math.pi)
    s.append(sakura)
    return s

SBManager = StoryboardManager('E:\\747823 Eisyo-kobu - Oriental Blossom', '123.osb')
camera = Camera2D()
camera.Move(1000, 2400, 300, 240, 340, 200)
camera.Rotate(1000, 2400, 0, math.pi)
s = Scene1()
s.set_camera(camera)
SBManager.append_scene(s, cmd_window=True)
SBManager.generate_storyboard(diff_specific=False)
