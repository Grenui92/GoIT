def all_sub_lists(data):
	result = [[]]
	for i in range(len(data)):
		for j in range(i+1, len(data)+1):
			result.append(data[i:j])
	return sorted(result, key=len)

print(all_sub_lists([4, 6, 1, 3]))