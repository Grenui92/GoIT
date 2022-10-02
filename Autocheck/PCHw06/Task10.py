def save_credentials_users(path, users_info):
	with open(path, 'wb') as file:
		for k, v in users_info.items():
			string = f'{k}:{v}\n'.encode()
			file.write(string)





save_credentials_users('Task10.csv', {'andry':'uyro18890D', 'steve':'oppjM13LL9e'})