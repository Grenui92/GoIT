def get_grade(key):
	return result.get(key, None)


def get_description(key):
	return result2.get(key, None)


litera = ['A', 'B', 'C', 'D', 'E', 'FX', 'F']
numbers = [5, 5, 4, 3, 3, 2, 1]
words = ['Perfectly', 'Very good', 'Good', 'Satisfactorily', 'Enough', 'Unsotisfactorily', 'Unsotisfactorily']
result = dict(zip(litera, numbers))
result2 = dict(zip(result, words))