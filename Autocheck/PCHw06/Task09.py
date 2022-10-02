def is_equal_string(utf8_string, utf16_string):
    utf8_string = utf8_string.decode('utf-8')
    utf16_string = utf16_string.decode('utf-16')
    return utf8_string == utf16_string

print(is_equal_string(b'hello', b'Hello Bro'))

