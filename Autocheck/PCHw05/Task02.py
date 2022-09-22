articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key: str, letter_case=False) -> dict:
	result = []
	for i in articles_dict:
		if letter_case:
			if key in str(i.values()):
				result.append(i)
		else:
			if key.lower() in str(i.values()).lower():
				result.append(i)
	return result

a = find_articles('Ocean')
for i in a:
	print(i)