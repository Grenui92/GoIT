from re import findall
def sanitize_phone_number(phone):
    return ''.join(findall(r'\d', phone))

print(sanitize_phone_number("    +38(050)123-32-34"))