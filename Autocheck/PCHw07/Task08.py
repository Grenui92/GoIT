import re
def token_parser(s: str):
	result = re.findall(r'(\d+|[+*\-()])', s)
	return result

print(token_parser('(2+ 3) *4 - 5 * 3'))