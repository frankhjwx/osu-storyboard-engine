from utils import *
from StoryboardCode import *
from StoryboardObject import *


class Scene:
    def __init__(self, *args):
        # Some unexplainable bugs raises when uses [] in func definition?
        if len(args) == 0:
            self.objects = []
        elif len(args) == 1:
            self.objects = args[0]
    
    def append(self, obj):
        self.objects.append(obj)

    def Move(self, *args):
        for obj in self.objects:
            obj.Move(args)

    def Vector(self, *args):
        for obj in self.objects:
            obj.Vector(args)

    def MoveX(self, *args):
        for obj in self.objects:
            obj.MoveX(args)

    def MoveY(self, *args):
        for obj in self.objects:
            obj.MoveY(args)

    def VectorX(self, *args):
        for obj in self.objects:
            obj.VectorX(args)

    def VectorY(self, *args):
        for obj in self.objects:
            obj.VectorY(args)

    def Fade(self, *args):
        for obj in self.objects:
            obj.Fade(args)

    def Rotate(self, *args):
        for obj in self.objects:
            obj.Rotate(args)

    def Scale(self, *args):
        for obj in self.objects:
            obj.Scale(args)

    def Color(self, *args):
        for obj in self.objects:
            obj.Color(args)

    def Parameter(self, *args):
        for obj in self.objects:
            obj.Parameter(args)

    def Loop(self, *args):
        for obj in self.objects:
            obj.Loop(args)

    def Trigger(self, *args):
        for obj in self.objects:
            obj.Trigger(args)

    def LoopOut(self):
        for obj in self.objects:
            obj.LoopOut()

    def print_scene(self, file_header = None):
        for obj in self.objects:
            obj.print_object(file_header)
