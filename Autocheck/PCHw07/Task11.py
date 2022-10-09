def sequence_buttons(string):
	dictionary = {'0': ' ', '1': ['.', ',', '?', '!', ':'], '2': ['A', 'B', 'C'], '3': ['D', 'E', 'F'], '4': ['G', 'H', 'I'],
	              '5': ['J', 'K', 'L'], '6': ['M', 'N', 'O'], '7': ['P', 'Q', 'R', 'S'], '8': ['T', 'U', 'V'], '9': ['W', 'X', 'Y', 'Z']}
	result = ''
	for i in string:
		for k, v in dictionary.items():
			if i.upper() in v:
				result += k*(v.index(i.upper())+1)
	return result




print(sequence_buttons("Hello, World!"))