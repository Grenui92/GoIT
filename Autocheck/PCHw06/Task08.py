def save_applicant_data(source, output):
	result = []
	for i in source:
		string = []
		for j in i:
			string.append(str(i[j]))
		result.append(','.join(string)+'\n')
	with open(output, 'w') as students:
		students.writelines(result)
	



slovar = [
    {   "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,},
    {   "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,},
    {   "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,},
]

save_applicant_data(slovar, 'Task08students.txt')