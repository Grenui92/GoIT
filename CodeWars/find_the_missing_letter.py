import string as str


def find_missing_letter(chars):
	for i, c in enumerate(chars):
		if c.isupper():
			l_upper = str.ascii_uppercase[str.ascii_uppercase.index(chars[0]):]
			if c != l_upper[i]:
				return l_upper[i]
		if c.islower():
			l_lower = str.ascii_lowercase[str.ascii_lowercase.index(chars[0]):]
			if c != l_lower[i]:
				return l_lower[i]



print(find_missing_letter(['O','Q','R','S']))
