def land_perimeter(arr):
	for k in arr:
		print(k)
	cnt = 0
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			if arr[i][j] == 'X':
				try:
					cnt += 1 if arr[i][j+1] == 'O' else 0
				except IndexError:
					cnt += 1
				try:
					cnt += 1 if arr[i][j-1] == 'O' or j-1 < 0 else 0
				except IndexError:
					cnt += 1
				try:
					cnt += 1 if arr[i+1][j] == 'O' else 0
				except IndexError:
					cnt += 1
				try:
					cnt += 1 if arr[i-1][j] == 'O' or i-1 < 0 else 0
				except IndexError:
					cnt += 1
	return f'Total land perimeter: {cnt}'
	
	
	
	
	
	
	
	
print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]))
#Total land perimeter: 60