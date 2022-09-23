def formatted_numbers():
	result = [f"|{'decimal' : ^10}|{'hex' : ^10}|{'binary' : ^10}|"]
	for i in range(16):
		result.append(f"|{i : <10}|{i : ^10x}|{i : >10b}|")
	return result
for el in formatted_numbers():
	print(el)