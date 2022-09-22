def solution(n: int):
	romans = ['I', 'X', 'C', 'M']
	romans_half = ['V', 'L', 'D', ]
	n_revers = list(str(n))[::-1]
	result = []
	for i, num in enumerate(n_revers):
		if int(num) <= 3:
			result.append(romans[i] * int(num))
		elif 3 < int(num) < 9:
			result.append(romans[i] * max(0, 5 - int(num)) + romans_half[i] + romans[i] * max(int(num) - 5, 0))
		elif int(num) == 9:
			result.append(romans[i] + romans[i + 1])
	return ''.join(result[::-1])


print(solution(int(input())))

