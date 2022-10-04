def is_integer(s: str):
	if s.isspace() or not s:
		return False
	else:
		return s.strip()[1:].isdigit() if s.strip()[0] in ['+', '-'] else s.strip().isdigit()

print(is_integer('           '))
	