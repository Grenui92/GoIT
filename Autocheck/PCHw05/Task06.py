import re
def is_spam_words(text, spam_words, space_around=False):
	return bool(re.findall(r'\b{}\b'.format(*spam_words), text)) if space_around else bool(re.findall(r'{}'.format(*spam_words), text))

print(is_spam_words("Молох", ["пиво","лох", "хол", "книга"]))