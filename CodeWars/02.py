def billboard(name, price=30):
    result = 0
    for _ in name:
        result += price
    return result
print(billboard('Jeong-Ho Aristotelis'))