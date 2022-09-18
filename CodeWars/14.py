# def duplicate_count(text):
#     char = []
#     result = ''
#     for i in text.lower():
#         if i not in char:
#             char.append(i)
#         elif i not in result:
#             result += i
#     return len(result)
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
print(duplicate_count("abcdeaB"))