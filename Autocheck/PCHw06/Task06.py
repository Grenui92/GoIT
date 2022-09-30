def get_recipe(path, search_id):
	result = {}
	with open(path, 'r') as file:
		for string in file.readlines():
			a, b, *c = string.strip().split(',')
			result.update({a: {'id': a, 'name': b, 'ingredients': c}})
	try:
		return result[search_id]
	except KeyError:
		return None

print(get_recipe("Task06.txt", "60b90c3b13067a15887e1ae4"))

			