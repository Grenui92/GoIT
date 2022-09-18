def to_jaden_case(string):
    return ' '.join([j[0].upper()+j[1:] for j in string.split()])


text = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(text))
