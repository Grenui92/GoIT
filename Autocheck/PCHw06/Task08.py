def save_applicant_data(source, output):
	result = []
	for i in source:
		string = []
		for j in i:
			string.append(str(i[j]))
		result.append(','.join(string)+'\n')
	print(result)
	with open(output, 'w') as students:
		students.writelines(result)
def save_applicant_data(source, output):
    with open(output, 'w') as fh:
        students_list = []
        for i in source:
            students_list.append(str(i['name']) + ',')
            students_list.append(str(i['specialty']) + ',')
            students_list.append(str(i['math']) + ',')
            students_list.append(str(i['lang']) + ',')
            students_list.append(str(i['eng']) + '\n')
            print(students_list)
        fh.writelines(students_list)
with open('Task08.txt') as file:
    for i in file.readlines():
        print(i)


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

save_applicant_data(slovar, 'Task08.txt')