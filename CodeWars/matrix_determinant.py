def determinant(matrix):
	n = len(matrix[0])
	m = len(matrix)
	fix =[]
	for i in range(n):
		if n > 2:
			result = []
			for j in range(n-1):
				result.append(matrix[j+1][1:])
			c = determinant(result)
		else:
			a = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
			return a
		fix.append(c)
	print(fix)
	
import numpy as np


# def determinant(matrix1):
# 	return round(np.linalg.det(np.matrix(matrix1)))
		
print(determinant([[2, 4, 2], [3, 1, 1], [1, 2, 0]]))
