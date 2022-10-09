def to_indexed(source_file, output_file):
	result = []
	with open(source_file, 'r') as file:
		for num, strin in enumerate(file.readlines()):
			result.append(f'{num}: {strin}')
	with open(output_file, 'w') as file:
		file.writelines(result)
		