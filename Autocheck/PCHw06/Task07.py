def sanitize_file(source, output):
	result = ''
	with open(source, 'r') as sour, open(output, 'w') as out:
		sour.seek(0)
		for i in sour.read():
			if not i.isdigit():
				result += i
		out.write(result)
			
			
			
sanitize_file('Task07source.txt', 'Task07output.txt')