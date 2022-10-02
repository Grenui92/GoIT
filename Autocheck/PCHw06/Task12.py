import base64
def get_credentials_users(path):
	with open(path, 'rb') as file:
		return [i.strip().decode() for i in file.readlines()]
	

def encode_data_to_base64(data):
	result = []
	for obj in data:
		obj = obj.encode()
		obj = base64.b64encode(obj).decode('utf-8')
		result.append(obj)
	return result
		
	
names = get_credentials_users('Task12.txt')
res = encode_data_to_base64(names)
print(res)