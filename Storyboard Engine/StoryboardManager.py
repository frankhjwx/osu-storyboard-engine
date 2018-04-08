from StoryboardScene import *
import os


class StoryboardManager:
    def __init__(self, map_folder_path, storyboard_filename, create_backup=False, restore_backup=False):
        self.map_folder_path = map_folder_path
        self.storyboard_filename = storyboard_filename
        self.storyboard_file = os.path.join(map_folder_path, storyboard_filename)
        self.scenes = []
        self.scene_file_headers = []
        self.background_images = []
        self.diff_specific_parts = {}
        self.diff_names = []
        self.restore = restore_backup
        if not os.path.exists(self.map_folder_path):
            raise RuntimeError('Map folder doesn\'t exist!')
        if create_backup:
            self.create_backup()
        if restore_backup:
            self.restore_backup()
            return
        self.storyboard_file_header = self.get_storyboard_file_header()
        self.diff_specific_headers = self.get_osu_file_headers()


    def set_bg(self, filename):
        # all bgs set here will be set hidden in storyboard
        if isinstance(filename, list):
            self.background_images.extend(filename)
        else:
            self.background_images.append(filename)

    def get_diff_names(self):
        return self.diff_names

    # file_header = None -> point to self.storyboard_file_header
    # file_header = '' -> print to cmd window
    # file_header = diff_specific_headers[?] -> point to a single diff
    # file_header = diff_name -> point to a single diff
    def append_scene(self, scene, file_header=None):
        if self.restore:
            return
        if file_header is None:
            file_header = self.storyboard_file_header
        self.scenes.append(scene)
        self.scene_file_headers.append(file_header)

    def generate_storyboard(self, diff_specific=False):
        if self.restore:
            return
        # deal with osb file first
        self.storyboard_file_header.write(
            '[Events]\n'
            '//Background and Video events\n')
        for img in self.background_images:
            self.storyboard_file_header.write('Sprite,Background,TopLeft,"' + img + '",0,0\n')
        self.storyboard_file_header.write(
            '//Storyboard Layer 0 (Background)\n'
            '//Storyboard Layer 1 (Fail)\n'
            '//Storyboard Layer 2 (Pass)\n'
            '//Storyboard Layer 3 (Foreground)\n')
        for i in range(len(self.scenes)):
            if self.scene_file_headers[i] == self.storyboard_file_header:
                self.scenes[i].print_scene(self.storyboard_file_header)
        self.storyboard_file_header.write('//Storyboard Sound Samples\n')
        if diff_specific:
            for diff_name in self.diff_names:
                for line in self.diff_specific_parts[diff_name][0]:
                    self.diff_specific_headers[diff_name].write(line)
                for i in range(len(self.scenes)):
                    if self.scene_file_headers[i] == self.diff_specific_headers[diff_name]:
                        self.scenes[i].print_scene(self.scene_file_headers[i])
                for line in self.diff_specific_parts[diff_name][2]:
                    self.diff_specific_headers[diff_name].write(line)

    def create_backup(self):
        backup_filename = os.path.join(self.map_folder_path, self.storyboard_filename.split('.')[0]+'.bak1')
        copy_file(self.storyboard_file, backup_filename)
        for (dir_path, _, file_names) in os.walk(self.map_folder_path):
            for fn in file_names:
                if '.osu' in fn:
                    backup_filename = os.path.join(dir_path, fn.split('.')[0] + '.bak2')
                    copy_file(os.path.join(dir_path, fn), backup_filename)

    def restore_backup(self):
        backup_filename = os.path.join(self.map_folder_path, self.storyboard_filename.split('.')[0]+'.bak1')
        if not os.path.exists(backup_filename):
            print(backup_filename)
            raise RuntimeError('Cannot restore a backup!')
        copy_file(backup_filename, self.storyboard_file)
        for (dir_path, _, file_names) in os.walk(self.map_folder_path):
            for fn in file_names:
                if '.osu' in fn:
                    backup_filename = os.path.join(dir_path, fn.split('.')[0] + '.bak2')
                    copy_file(backup_filename, os.path.join(dir_path, fn))

    def get_storyboard_file_header(self):
        file_header = open(self.storyboard_file, 'w', encoding='utf-8', errors='ignore')
        return file_header

    def get_osu_file_headers(self):
        diff_paths = []
        for (dir_path, _, file_names) in os.walk(self.map_folder_path):
            for fn in file_names:
                if '.osu' in fn:
                    diff_paths.append(os.path.join(dir_path, fn))
        headers = {}
        for path in diff_paths:
            f = open(path, 'r', encoding='utf-8', errors='ignore')
            parts = [[], [], []]
            status = 0
            # before:0 sb:1 after:2
            diff_name = ''
            while 1:
                line = f.readline()
                if not line:
                    break
                if line == '//Storyboard Sound Samples\n':
                    status += 1
                parts[status].append(line)
                if line == '//Storyboard Layer 3 (Foreground)\n':
                    status += 1
                if 'Version:' in line:
                    diff_name = line.split(':')[1][:-1]
            headers[diff_name] = open(path, 'w', encoding='utf-8', errors='ignore')
            self.diff_specific_parts[diff_name] = parts
            self.diff_names.append(diff_name)
        return headers

    def delete_backups(self):
        for (dir_path, _, file_names) in os.walk(self.map_folder_path):
            for fn in file_names:
                if '.bak' in fn:
                    os.remove(os.path.join(dir_path, fn))

