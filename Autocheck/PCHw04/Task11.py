def is_valid_password(password: str) -> bool:
	"""Chek password to be correct

	correct == upper, lower, number is in password. Len >= 8"""
	flag_low = False
	flag_upp = False
	flag_num = False
	for i in password:
		if i.islower():
			flag_low = True
		elif i.isupper():
			flag_upp = True
		elif i.isdigit():
			flag_num = True
	return True == flag_num == flag_low == flag_upp if len(password)>= 8 else False