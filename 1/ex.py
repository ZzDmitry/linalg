import sys

input = sys.stdin.read()
numbers = input.split()
number_i = 0

def get_num():
	global number_i
	value = int(numbers[number_i])
	number_i = number_i + 1
	return value

rows = get_num()
cols = get_num()

if rows < cols:
	print('INF')
	exit()

matrix = []
right = rows*[0]

for row in range(0, rows):
	matrix.append([])
	for col in range(0, cols):
		matrix[row].append(get_num())
	right[row] = get_num()
#print(matrix)
#print(right)

def rid_of_col(matrix, n):
	for row in range(n + 1, len(matrix)):
		mul = matrix[row][n] / matrix[n][n]
		for col in range(n, len(matrix[row])):
			matrix[row][col] = matrix[row][col] - matrix[n][col] * mul

#for row in range(1, rows):
#	mul = 1

for n in range(0, rows):
	rid_of_col(matrix, n)
print(matrix)