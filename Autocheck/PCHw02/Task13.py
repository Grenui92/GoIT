from string import *
message = 'Hello my little friends!'
offset = 37
encoded_message = ""
u, l = ascii_uppercase, ascii_lowercase
for ch in message:
    if ch.isalpha():
        ch = u[(u.index(ch)+offset)%len(u)] if ch.isupper() else l[(l.index(ch)+offset)%len(l)]
    encoded_message += ch
print(encoded_message)