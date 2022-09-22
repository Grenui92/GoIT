def next_bigger(n: int):
	print(n)
	str_n = [i for i in str(n)][::-1]
	for i, ch in enumerate(str_n):
		try:
			if int(str_n[i])>int(str_n[i+1]):
				str_n[i], str_n[i+1] = str_n[i+1], str_n[i]
				break
		except IndexError:
			return -1
	return int(''.join(reversed(str_n)))

print(next_bigger(531))