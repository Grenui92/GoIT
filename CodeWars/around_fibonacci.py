def around_fib(n):
	print(n)
	fib = [0, 1, 1]
	for i in range(n-2):
		fib.append(fib[-2]+fib[-1])
	num = str(fib[-1])
	result = {i : num.count(str(i)) for i in range(10)}
	obrez = len(num[25:])
	k = num[-(len(num)%25):] if len(num)%25 != 0 else num[-25:]
	return f'Last chunk {k}; Max is {result[max(result, key=result.get)]} for digit {max(result, key=result.get)}'


print(around_fib(int(input())))
