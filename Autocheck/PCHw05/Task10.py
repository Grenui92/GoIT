import re


def find_word(text, word):
	a = re.search(word, text)
	result = {'result': bool(a) == True,
	          'first_index': a.span()[0] if a else None,
	          'last_index': a.span()[1] if a else None,
	          'search_string': word,
	          'string': text}
	return result


	




print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "python"))