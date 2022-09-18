def sum_dig_pow(a, b):
	return [j for j in range(a,b+1) if sum([int(n)**i for i, n in enumerate(str(j), 1)]) == j]


print(sum_dig_pow(89, 135))
