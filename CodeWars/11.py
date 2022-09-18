def expanded_form(num):
	s = str(num)
	return ' + '.join(j+'0'*(len(s)-i-1) for i,j in enumerate(s) if j != '0')

print(expanded_form(123456))