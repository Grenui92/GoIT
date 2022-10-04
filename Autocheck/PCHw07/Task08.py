import re
def token_parser(s: str):
	result = re.findall(r'(\d+|[+*\-()])', s)
	# result =[]
	# elem = ''
	# for i in s:
	# 	if i.isdigit():
	# 		elem += i
	# 	elif i.isspace():
	# 		continue
	# 	else:
	# 		result.append(elem)
	# 		result.append(i)
	# 		elem = ''
	# if elem:
	# 	result.append(elem)
	return result



print(token_parser('(2+ 3) *4 - 5 * 3'))