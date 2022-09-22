def gap(g, m, n):
    x, y = None, None #дві змінні яким потім присвоїм прості числа
    for i in range(m, n+1):
        cnt = 0
        for j in range(1,i): #цикл щоб порахувати скільки дільникі у і (просте число - всього 2)
            if i%j == 0:
                cnt += 1
            if cnt > 2 or j*j >= n:
                break
        try: #виняток якщо у або х не Інт
            if cnt < 2:
                x, y = i, x #потрохи заміняємо наші змінні на прості числа
            if x-y == g:
                return [y, x]
        except TypeError:
            continue
    return None

print(gap(4,100,110))