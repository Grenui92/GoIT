import re
def is_spam_words(text, spam_words, space_around=False):
    result = []
    for i in spam_words:
        if space_around:
            result.append(bool(re.findall(r'\b{}\b'.format(i), text)))
        else:
            result.append(bool(re.findall(r'{}'.format(i), text)))
    return any(result)

print(is_spam_words("Молох", ["лох","пиво","лох", "хол", "книга"]))