def data_preparation(list_data: list):
	list_data_new = []
	for data in list_data:
		if len(data) >2:
			data.remove(max(data))
			data.remove(min(data))
			list_data_new.extend(data)
		else:
			list_data_new.extend(data)
	return sorted(list_data_new, reverse=True)




print(data_preparation([[1,2,3],[3,4], [5,6]]))