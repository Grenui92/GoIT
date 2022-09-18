def format_ingredients(items):
	return ', '.join(items[:-1]) + ' and ' + items[-1] if len(items) > 1 else ''.join(items)


def format_ingredients(items):
	result = ''
	if len(items) <= 1:
		for i in items:
			result += i
		return result
	else:
		for i in items[:-2]:
			result += i + ', '
		result += items[-2] + ' and ' + items[-1]
		return result


print(format_ingredients([]))
