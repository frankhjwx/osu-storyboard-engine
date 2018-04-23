from Storyboard.StoryboardObject import *
import numpy as np


class Scene:
    def __init__(self, *args):
        # Some unexplainable bugs raises when uses [] in func definition?
        if len(args) == 0:
            self.objects = []
        elif len(args) == 1:
            self.objects = args[0]
        self.camera = None
    
    def append(self, obj):
        if isinstance(obj, list):
            self.objects.extend(obj)
        elif isinstance(obj, Object):
            self.objects.append(obj)
        elif isinstance(obj, Scene):
            self.objects.extend(obj.objects)

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

    def set_camera(self, camera):
        self.camera = camera

    def print_scene(self, file_header=None):
        # Not in Camera2D mode
        if self.camera is None:
            for obj in self.objects:
                obj.print_object(file_header)

        # Camera2D
        else:
            for obj in self.objects:
                obj.get_start_end_t()
                start_t = obj.start_t
                end_t = obj.end_t
                SceneObj = Object(obj.file_name, obj.object_type, obj.layer, obj.origin, obj.x, obj.y, obj.frame_count,
                                  obj.frame_delay, obj.loop_type)
                for code in obj.codes:
                    if code.key == 'C' or code.key == 'P' or code.key == 'L' or code.key == 'T':
                        SceneObj.append(code)
                timestamps = []
                for t in range(start_t, end_t, int(1000/self.camera.fps)):
                    timestamps.append(t)
                timestamps.append(end_t)
                view_pos_list = []
                view_vector_list = []
                view_rotation_list = []
                for t in timestamps:
                    obj_pos = obj.get_position(t)
                    obj_vector = obj.get_scale(t)
                    obj_rotation = obj.get_rotation(t)
                    cam_pos = self.camera.get_position(t)
                    cam_scale = self.camera.get_scale(t)
                    cam_rotation = self.camera.get_rotation(t)
                    # change coordinate system
                    obj_pos = [obj_pos[0] - 320, obj_pos[1] - 240]
                    cam_pos = [cam_pos[0] - 320, cam_pos[1] - 240]
                    rotate = np.array([[math.cos(cam_rotation), math.sin(cam_rotation), 0],
                                       [-math.sin(cam_rotation), math.cos(cam_rotation), 0],
                                       [0, 0, 1]])
                    transition = np.array([[1, 0, 0],
                                           [0, 1, 0],
                                           [cam_pos[0], cam_pos[1], 1]])
                    scale = np.array([[cam_scale, 0, 0],
                                      [0, cam_scale, 0],
                                      [0, 0, 1]])
                    view_pos = np.dot(np.array([obj_pos[0], obj_pos[1], 1]), (np.dot(rotate, np.dot(transition, scale))))
                    # return to the original system
                    view_pos = [view_pos[0] + 320, view_pos[1] + 240]

                    view_vector = [obj_vector[0]*cam_scale, obj_vector[1]*cam_scale]
                    view_rotation = obj_rotation + cam_rotation

                    view_pos_list.append(view_pos)
                    view_vector_list.append(view_vector)
                    view_rotation_list.append(view_rotation)
                    if len(view_pos_list) > 1:
                        k = len(view_pos_list)
                        SceneObj.Move(timestamps[k-2], timestamps[k-1], view_pos_list[k-2], view_pos_list[k-1])
                        SceneObj.Vector(timestamps[k-2], timestamps[k-1], view_vector_list[k-2], view_vector_list[k-1])
                        SceneObj.Rotate(timestamps[k-2], timestamps[k-1], view_rotation_list[k-2], view_rotation_list[k-1])
                SceneObj.print_object(file_header)

