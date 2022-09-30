def get_cats_info(path):
	with open(path, 'r') as file:
		result = []
		for string in file.readlines():
			a, b, c = string.strip().split(',')
			result.append({'id': a, 'name': b, 'age': c})
	return result
		
for i in get_cats_info('Task05.txt'):
	print(i)
