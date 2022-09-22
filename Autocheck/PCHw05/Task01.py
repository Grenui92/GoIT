def real_len(text):
    l = 0
    for ch in text:
        l += 1 if ch not in  '\n\f\r\t\v' else 0
    return l

print(real_len('Alex\nKdfe23\t\f\v.\r'))
print(len(r'Alex\nKdfe23\t\f\v.\r'))