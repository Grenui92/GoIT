import re
def decode(data):
    def repl(a):
        b = a.group()
        return b[0] * int(b[1:])
    data = ''.join(str(i) for i in data)
    return list(re.sub(r'\S\d+', repl, data))
    
# def repl(a):
#     b = a.group()
#     return b[0]*int(b[1:])
    



print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))
'"X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2'