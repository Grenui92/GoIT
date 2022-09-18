def is_valid_pin_codes(pin_codes):
	print(pin_codes)
	flag = len(set(pin_codes)) == len(pin_codes) if len(pin_codes) != 0 else False
	if flag:
		for i in pin_codes:
			if type(i) != str:
				flag = False
				break
			if i.isdigit() == False:
				flag = False
				break
			if len(i) != 4:
				flag = False
				break
	return flag

print(is_valid_pin_codes(['1101', '9034', 3001]))
print(set(['1101', '9034', '0011', '1101']))