from re import findall
def format_phone_number(funcs):
    def wrapper(phone):
        num = funcs(phone)
        if len(num) == 10:
            return f'+38{num}'
        elif len(num) == 12:
            return f'+{num}'
    return wrapper

@format_phone_number
def sanitize_phone_number(phone):
    return ''.join(findall(r'\d', phone))


for i in ["    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",]:
    print(sanitize_phone_number(i))