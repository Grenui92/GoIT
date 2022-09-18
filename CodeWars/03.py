def spin_words(sentence):
    sentence = [i[::-1]  if len(i)>=5 else i for i in sentence.split()]
    return ' '.join(sentence)

text = input()
print(spin_words(text))