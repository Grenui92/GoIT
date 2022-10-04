def data_preparation(list_data: list):
	result = []
	for i in list_data:
		if len(i) >2:
			i.remove(max(i))
			i.remove(min(i))
			result.extend(i)
		else:
			result.extend(i)
	return sorted(result, reverse=True)




print(data_preparation([[1,2,3],[3,4], [5,6]]))