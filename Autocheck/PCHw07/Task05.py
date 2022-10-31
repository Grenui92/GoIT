import re
def capital_text(s):
	return re.sub(r"([.!?\n]{1} \w|[.!?\n]{1}\w|^\w)", lambda x: f'{x.group()[:-1]}{x.group()[-1].upper()}', s.strip())

# def reper(m):
# 	return f'{m.group()[:-1]}{m.group()[-1].upper()}'



text = '      english texts for beginners to practice reading and comprehension online and for free. practicing your comprehension of ' \
       'written ' \
       'English will both improve your vocabulary and understanding of grammar and word order? the texts below are designed to help you ' \
       'develop while giving you an instant evaluation\n of your progress! sex bomb may be beautiful.asdasfawerwqerqwer!sdfsdfsg'

print(capital_text(text))
#lambda x: f"{x[:-1]}{x[-1].upper()}"
