message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    new_char = ch
    if ch.isalpha():
        if ch.isupper():
            pos = (ord(ch) - ord('A') + offset) % 26
            new_char = chr(pos + ord("A"))
        elif ch.islower():
            pos = (ord(ch) - ord('a') + offset) % 26 
            new_char = chr(pos + ord("a"))
    encoded_message += new_char
print(encoded_message)