def get_credentials_users(path):
	with open(path, 'rb') as file:
		return [i.strip().decode() for i in file.readlines()]