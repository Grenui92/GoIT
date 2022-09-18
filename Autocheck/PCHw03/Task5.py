def get_fullname(first, last, middle_name = '', ):
    if middle_name:
        return f'{first} {middle_name} {last}'
    else:
        return f'{first} {last}'