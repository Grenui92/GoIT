def snail(snail_map):
	n, m = (int(i) for i in input().split())
	mtrx = [[0 for i in range(1, m + 1)] for j in range(n)]
	cnt = 0
	dl_stroki, vs_stolba = m - 1, n - 1
	i, j, s = 0, -1, 0
	flag = False
	if n == 1 or m == 1:
		for i in range(n):
			for j in range(m):
				mtrx[i][j] = cnt + 1
				cnt += 1
	while cnt < m * n:
		if dl_stroki <= 0 or vs_stolba <= 0:
			mtrx[n // 2][m // 2] = cnt + 1
			cnt += 1
		for _ in range(dl_stroki):
			cnt += 1
			j += 1
			mtrx[i][j] = cnt
		j += 1
		i -= 1
		for _ in range(vs_stolba):
			cnt += 1
			i += 1
			mtrx[i][j] = cnt
		i += 1
		j += 1
		for _ in range(dl_stroki):
			cnt += 1
			j -= 1
			mtrx[i][j] = cnt
		i += 1
		j -= 1
		for _ in range(vs_stolba):
			cnt += 1
			i -= 1
			mtrx[i][j] = cnt
		vs_stolba -= 2
		dl_stroki -= 2
	
	for row in mtrx:
		for c in row:
			print(str(c).ljust(3), end=' ')
		print()
	return snail_map


print(snail([[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]))