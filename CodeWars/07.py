def to_camel_case(text):
    if text:
        text = text.replace('-', ' ')
        text = text.replace('_', ' ')
        text = [c[0].upper()+c[1:].lower() if i >= 1 else c for i,c in enumerate(text.split(' '))]
        return ''.join(text)
    return ''.join(text)


print(to_camel_case("the_stealth_warrior"))