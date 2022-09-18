def first_non_repeating_letter(string: str):
    result = {(string.count(c), i): c for i, c in enumerate(string) if string.lower().count(c.lower()) == 1}
    return result[min(result)] if result else ''

print(first_non_repeating_letter('sTreSS'))
