import re

def is_spam_words(text, spam_words, space_around=False):
    if space_around:
        for i in spam_words:
            my_reg = r"[\s| ]" + re.escape(i) + "[ |.]"
            return True if re.findall(my_reg, text, re.I) else False
    else:
        for i in spam_words:
            my_reg = re.escape(i)
            return True if re.findall(my_reg, text, re.I) else False

print(is_spam_words("Молох", ["лох","пиво","лох", "хол", "книга"]))