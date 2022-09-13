work_experience = int(input("Enter your full work experience in years: "))

if work_experience <= 1:
    developer_type = "Junior"
elif 1 < work_experience <= 5:
    developer_type = "Middle"
else:
    developer_type = "Senior"