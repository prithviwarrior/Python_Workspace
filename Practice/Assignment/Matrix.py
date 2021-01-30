
L1 = [[1,2,3],[4,5,6],[7,8,9]]
L2 = [[1,2,3],[4,5,6],[7,8,9]]
L = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(L1)):
	
	for j in range(len(L2)):
		count = 0
		for k in range(j, len(L2)):
			count += (L1[i][k] * L2[k][j])
			L[i][j] = count

print(L)
