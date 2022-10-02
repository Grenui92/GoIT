import sys
import pathlib
import os

def first_start(folders: dict, path_to_create: str):
	"""Здесь будут создаваться папки вк оторые будут складываться файлы, запускаться основная функция."""
	
	for folder in new_absolute_folders_create():
		try:
			os.mkdir(f'{path_to_create}/{folder}')
		except FileExistsError:
			continue
	file_cheker(path_to_create)
	
	
	
def file_path() -> str:
	"""Получаем аргумент вызова для передачи в первый path"""
	
	return sys.argv[1]


def normilize(name: str) -> str:
	"""По идее должна вызываться из функции file_cheker() весте с именем, которое мы
	будем обрабатывать. Вернет уже обработанное имя и само переименование уже будет происходить в file_cheker()"""
	
	name = name.translate(translate_map)
	for i in name:
		if not i.isdigit() and not i.isalpha():
			name = name.replace(i, '_')
	return name
			
	
	
def file_cheker(path):
	"""Основная функция в которой будем бежать по файлам, рекурсировать, если будут вложенные папки,
	 и выполнять сортировку"""
	
	
	p = pathlib.Path(path)
	for item in p.iterdir():
		if item.is_dir() and item.name not in absolute_folders:
			file_cheker(f'{p}/{item.name}')
			new_name = normilize(item.name)
			item.rename(pathlib.Path(f'{p}/{new_name}'))
		elif item.is_file():
			new_name = normilize(item.stem) #Отправляем файл на нормализацию имени
			if item.suffix[1:] in absolute_folders['archives']:
				item.rename(pathlib.Path(f'{main_path}/archives/{new_name}{item.suffix}'))
			elif item.suffix[1:] in absolute_folders['video']:
				item.rename(pathlib.Path(f'{main_path}/video/{new_name}{item.suffix}'))
			elif item.suffix[1:] in absolute_folders['audio']:
				item.rename(pathlib.Path(f'{main_path}/audio/{new_name}{item.suffix}'))
			elif item.suffix[1:] in absolute_folders['documents']:
				item.rename(pathlib.Path(f'{main_path}/documents/{new_name}{item.suffix}'))
			elif item.suffix[1:] in absolute_folders['images']:
				item.rename(pathlib.Path(f'{main_path}/images/{new_name}{item.suffix}'))
			elif item.suffix[1:] in absolute_folders['torrent']:
				item.rename(pathlib.Path(f'{main_path}/torrent/{new_name}{item.suffix}'))
			elif item.suffix[1:] in absolute_folders['programs']:
				item.rename(pathlib.Path(f'{main_path}/programs/{new_name}{item.suffix}'))
			else:
				item.rename(pathlib.Path(f'{main_path}/others/{new_name}{item.suffix}'))
	for item in p.iterdir():
		if item.name not in absolute_folders:
			try:
				item.rmdir()
			except OSError:
				file_cheker(main_path)
				

def new_absolute_folders_create() -> dict:
	absolute_folders = {'archives': ['zip', 'gz', 'tar'], 'video': ['avi', 'mp4', 'mov', 'mkv'], 'audio': ['mp3', 'ogg', 'wav', 'amr'],
	                    'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'], 'images': ['jpeg', 'png', 'jpg', 'svg'], 'others': [],
	                    'torrent': ['torrent'], 'programs': ['exe']}
	print("Вот по таким папкам в соответствии с расширениями будут отсортированы файлы:")
	for k, v in absolute_folders.items():
		print(f'Папка {k} будет включать в себя файлы с расширением {v}')
	print('Можно добавить интересующие вас папки, по которым будут рассортированы файлы.')
	while True:
		name = input('*****\n'
		             'Если хотите добавить расширение - с начала введите название существующей папки. \n'
		             'Если хотите создать новую папку - введите ее название. \n'
		             'Принимаются только буквы латиницы и цифры.\n'
		             'Если не хотите предпринимать никаких действий - введите STOP: ')
		if name == 'STOP':
			break
		if not name.isalnum():
			print(f'Введенные данные {name} не соответствую требованиям (принимаются только латинские буквы и цифры). Попробуйте вновь.')
			continue
		absolute_folders.setdefault(name, []).append(input(f'Введите расширение чтоб добавить в папку {name}: '))
	return absolute_folders

def new_translate_map() -> dict:
	translate_map = {1040: 'A', 1041: 'B', 1042: 'V', 1043: 'G', 1044: 'D', 1045: 'E', 1046: 'GH', 1047: 'Z',
	                 1048: 'I', 1049: 'J', 1050: 'K', 1051: 'L', 1052: 'M', 1053: 'N', 1054: 'O', 1055: 'P',
	                 1056: 'R', 1057: 'S', 1058: 'T', 1059: 'U', 1060: 'F', 1061: 'H', 1062: 'TS', 1063: 'CH',
	                 1064: 'SH', 1065: 'SH', 1066: '', 1067: 'I', 1068: '', 1069: 'E', 1070: 'YU', 1071: 'YA',
	                 1025: 'YO', 1072: 'a', 1073: 'b', 1074: 'v', 1075: 'g', 1076: 'd', 1077: 'e', 1078: 'gh',
	                 1079: 'z', 1080: 'i', 1081: 'j', 1082: 'k', 1083: 'l', 1084: 'm', 1085: 'n', 1086: 'o',
	                 1087: 'p', 1088: 'r', 1089: 's', 1090: 't', 1091: 'u', 1092: 'f', 1093: 'h', 1094: 'ts',
	                 1095: 'ch', 1096: 'sh', 1097: 'sh', 1098: '', 1099: 'i', 1100: '', 1101: 'e', 1102: 'yu',
	                 1103: 'ya', 1105: 'yo'}
	return translate_map

if __name__ == '__main__':
	absolute_folders = new_absolute_folders_create()
	translate_map = new_translate_map()
	main_path = file_path()
	first_start(absolute_folders, main_path)