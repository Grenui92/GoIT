def snail(mtrx):
    n, m = len(mtrx), len(mtrx[0])
    result = []
    dl_stroki, vs_stolba = m - 1, n - 1
    i, j = 0, -1
    cnt = 0
    if n == 1 or m == 1:
        for i in range(n):
            for j in range(m):
                result.append(mtrx[i][j])
                cnt += 1
    while cnt < m * n:
        if dl_stroki <= 0 or vs_stolba <= 0:
            result.append(mtrx[n // 2][m // 2])
            cnt += 1
        for _ in range(dl_stroki):
            cnt += 1
            j += 1
            result.append(mtrx[i][j])
        j += 1
        i -= 1
        for _ in range(vs_stolba):
            cnt += 1
            i += 1
            result.append(mtrx[i][j])
        i += 1
        j += 1
        for _ in range(dl_stroki):
            cnt += 1
            j -= 1
            result.append(mtrx[i][j])
        i += 1
        j -= 1
        for _ in range(vs_stolba):
            cnt += 1
            i -= 1
            result.append(mtrx[i][j])
        vs_stolba -= 2
        dl_stroki -= 2
    return result
    # for row in mtrx:
    #     for c in row:
    #         print(str(c).ljust(3), end=' ')
    #     print()
    # return result

print(snail([[1,2,3], [8,9,4], [7,6,5]]))
print(snail([[1,2,3], [4,5,6], [7,8,9]]))