def formatted_grades(students):
	result = ['{:>4}|{:<10}|{:^5}|{:^5}'.format(i, c, students[c], grades[students[c]]) for i, c in enumerate(students.keys(), 1)]
	return result
	# for i, c in enumerate(students.keys(),1):
	# 	print('{:>4}|{:<10}|{:^5}|{:^5}'.format(i, c, students[c], grades[students[c]]))
	# 	# print('{:d}|{:d}{:s}{:d}'.format(c, i, students[c],grades[students[c]]))
	# return
grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
print(formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}))