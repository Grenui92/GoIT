import random
def create_phone_number(n):
    result = [str(i) for i in n]
    return f"({''.join(result[:3])}) {''.join(result[3:6])}-{''.join(result[6:])}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))