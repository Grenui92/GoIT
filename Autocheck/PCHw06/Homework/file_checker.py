import sys
import pathlib
import os

def first_start(folders: list, path_to_create: str):
	"""Здесь будут создаваться папки вк оторые будут складываться файлы, запускаться основная функция."""
	
	for folder in folders:
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
	print(p)
	for item in p.iterdir():
		print(item)
		if item.is_dir() and item.name not in absolute_folders:
			file_cheker(f'{p}/{item.name}')
		elif item.is_file():
			print('1')
			new_name = normilize(item.stem) #Отправляем файл на нормализацию имени
			print(new_name)
			try:
				os.rename(item, f'{new_name}{item.suffix}')
			except:
				continue
			print(item)

if __name__ == '__main__':
	absolute_folders = {'archives': ('ZIP', 'GZ', 'TAR'), 'video': ('AVI', 'MP4', 'MOV', 'MKV'),  'audio': ('MP3', 'OGG', 'WAV', 'AMR'),
	                   'documents': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'), 'images': ['JPEG', 'PNG', 'JPG', 'SVG']}
	translate_map = {1040: 'A', 1041: 'B', 1042: 'V', 1043: 'G', 1044: 'D', 1045: 'E', 1046: 'GH', 1047: 'Z',
	                 1048: 'I', 1049: 'J', 1050: 'K', 1051: 'L', 1052: 'M', 1053: 'N', 1054: 'O', 1055: 'P',
	                 1056: 'R', 1057: 'S', 1058: 'T', 1059: 'U', 1060: 'F', 1061: 'H', 1062: 'TS', 1063: 'CH',
	                 1064: 'SH', 1065: 'SH', 1066: '', 1067: 'I', 1068: '', 1069: 'E', 1070: 'YU', 1071: 'YA',
	                 1025: 'YO', 1072: 'a', 1073: 'b', 1074: 'v', 1075: 'g', 1076: 'd', 1077: 'e', 1078: 'gh',
	                 1079: 'z', 1080: 'i', 1081: 'j', 1082: 'k', 1083: 'l', 1084: 'm', 1085: 'n', 1086: 'o',
	                 1087: 'p', 1088: 'r', 1089: 's', 1090: 't', 1091: 'u', 1092: 'f', 1093: 'h', 1094: 'ts',
	                 1095: 'ch',  1096: 'sh', 1097: 'sh', 1098: '', 1099: 'i', 1100: '', 1101: 'e', 1102: 'yu',
	                 1103: 'ya', 1105: 'yo'}

	main_path = 'Downloads'
	first_start(absolute_folders, main_path)