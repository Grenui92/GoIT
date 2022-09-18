def dig_pow(n, p):
    cnt = 0
    result = 0
    for i in str(n):
        result += int(i)**(p+cnt)
        cnt += 1
        print(result)
    return result/n if result%n == 0 else -1


print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))