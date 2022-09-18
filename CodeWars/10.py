def find_outlier(n):
	result = [[], []]
	for i in n:
		if i % 2 == 0:
			result[0].append(i)
		else:
			result[1].append(i)
	if len(result[0]) > len(result[1]):
		return result[1][0]
	else:
		return result[0][0]


text = [2, 4, 0, 100, 4, 11, 2602, 36]
print(find_outlier(text))
