from pathlib import Path


def parse_folder(path):
	print(path)
	files = [i.name for i in path.iterdir() if i.is_file()]
	folders = [i.name for i in path.iterdir() if i.is_dir()]
	
	return files, folders