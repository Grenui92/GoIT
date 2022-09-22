import re
def is_check_name(fullname, first_name):
	result = re.findall(r'{}'.format(first_name), fullname)
	return bool(result)

print(is_check_name('Max Old', 'Alex'))