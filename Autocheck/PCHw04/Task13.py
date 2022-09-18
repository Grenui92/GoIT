from pathlib import *
def parse_folder(path):
	files = [i for i in path.iterdir() if i.is_file()]
	folders = [i for i in path.iterdir() if i.is_dir()]
	
	return files, folders