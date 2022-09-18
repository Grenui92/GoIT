def format_string(string, length):
	if len(string) >= length:
		return string
	else:
		return f"{' '*((length-len(string))//2)}{string}"
print(format_string(length = 15, string = 'abaa'))