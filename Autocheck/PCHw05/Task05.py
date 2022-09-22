from re import findall
def sanitize_phone_number(phone):
	return ''.join(findall(r'\d', phone))


def get_phone_numbers_for_countries(list_phones):
	spisok = [sanitize_phone_number(i) for i in list_phones]
	slovar = {'UA': [], 'SG': [], 'JP': [], 'TW': []}
	for i in spisok:
		if i.startswith('886'):
			slovar['TW'].append(i)
		elif i.startswith('65'):
			slovar['SG'].append(i)
		elif i.startswith('81'):
			slovar['JP'].append(i)
		else:
			slovar['UA'].append(i)
	return slovar


print(get_phone_numbers_for_countries(['380998759405', '818765347', '8867658976', '657658976']))
