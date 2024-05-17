from settings import * 
from os import walk
from os.path import join

def import_image(*path, alpha = True, format = 'png'):
	full_path = join(*path) + f'.{format}'
	return pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert_alpha()

def import_folder(*path):
	frames = []
	for folder_path, subfolders, image_names in walk(join(*path)):
		for image_name in sorted(image_names, key = lambda name: int(name.split('.')[0])):
			full_path = join(folder_path, image_name)
			frames.append(pygame.image.load(full_path).convert_alpha())
	return frames 

def import_folder_dict(*path):
	frame_dict = {}
	for folder_path, _, image_names in walk(join(*path)):
		for image_name in image_names:
			full_path = join(folder_path, image_name)
			surface = pygame.image.load(full_path).convert_alpha()
			frame_dict[image_name.split('.')[0]] = surface
	return frame_dict

def import_sub_folders(*path):
	frame_dict = {}
	for _, sub_folders, __ in walk(join(*path)): 
		if sub_folders:
			for sub_folder in sub_folders:
				frame_dict[sub_folder] = import_folder(*path, sub_folder)
	return frame_dict

class Animation:
	def __init__(self, images, frame_time):
		self.images = images
		self.image_index = 0
		self.image = self.images[self.image_index]
		self.frame_time = frame_time
		self.timer = 0

	def update(self):
		self.timer += 1
		self.image = self.images[self.image_index]
		if (self.timer > self.frame_time):
			if self.image_index < len(self.images) - 1:
				self.image_index += 1
			else:
				self.image_index = 0
			self.timer = 0