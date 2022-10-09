def encode(data):
    result = []
    cnt = 0
    for num, ch in enumerate(data, 1):
        cnt += 1
        if num == len(data):
            result.extend((ch, num))
            return result
        elif ch != data[num]:
            a = encode(data[num:])
            result.extend((ch, num , *a))
            return result
    return result




print(encode("XXXZZXXYYYZZ"))