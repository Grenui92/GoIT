import shutil


def create_backup(path, file_name, employee_residence):
	with open(f'{path}/{file_name}', 'wb') as file:
		for k, v in employee_residence.items():
			file.write(f'{k} {v}\n'.encode())
	archive_name = shutil.make_archive(file_name, 'zip', path)
	return archive_name




print(create_backup('Test_folder', 'Backup_folder', {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}))