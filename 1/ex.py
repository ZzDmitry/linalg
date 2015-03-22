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

matrix = []
right = rows * [0]

for row in range(0, rows):
	matrix.append([])
	for col in range(0, cols):
		matrix[row].append(get_num())
	right[row] = get_num()

def stringify_matrix(m, r, prec):
	def format_num(n, prec):
		return ('{0:.' + str(prec) + 'f}').format(n)
	def calc_num_width(n, prec):
		return len(format_num(n, prec))
	def calc_row_width(ns, prec):
		w = 0 
		for i in range(0, len(ns)):
			wi = calc_num_width(ns[i], prec)
			if wi > w:
				w = wi
		return w
	def calc_matrix_width(m, prec):
		w = 0
		for row in range(0, len(m)):
			w_row = calc_row_width(m[row], prec)
			if w_row > w:
				w = row
		return w
	w = calc_matrix_width(m, prec)
	rw = calc_row_width(r, prec)
	#print([1111111, m, r, prec, w, rw])
	def str_num(n, prec, w):
		#print(['str_num', n, prec, w])
		s = format_num(n, prec)
		padding = ' ' * (w - len(s))
		return padding + s
	def str_row(row, prec, w, r, w_r):
		#print(['str_row', row, prec, w, r, w_r])
		s = ''
		for i in range(0, len(row)):
			if i != 0:
				s = s + '  '
			s = s + str_num(row[i], prec, w)
		s = s + ' | ' + str_num(r, prec, w_r)	
		return s
	s = ''
	for i in range (0, len(m)):
		s = s + str_row(m[i], prec, w, r[i], rw) + '\n'
	return s
	
#print(stringify_matrix(matrix, right, 1))
#print(stringify_matrix(matrix, right, 2))
#print(stringify_matrix(matrix, right, 3))
#print(stringify_matrix(matrix, right, 4))
#print(stringify_matrix(matrix, right, 0))
#exit()

# return row of first nonzero element starting with matrix[n][n] and down
# or return -1
def find_nonzero(matrix, r, c):
	for row in range(r, len(matrix)):
		if matrix[row][c] != 0:
			return row
	return -1

# swap matrixes and right parts rows	
def swap_rows(matrix, right, r1, r2):
	row1 = matrix[r1]
	matrix[r1] = matrix[r2]
	matrix[r2] = row1
	row1 = right[r1]
	right[r1] = right[r2]
	right[r2] = row1

# leave non-zero matrix[n][n] or make it swapping two lines
# return False if it has only zeros
# that means infinite solutions
def make_nonzero_base(matrix, right, r, c):
	nonzero_row = find_nonzero(matrix, r, c)
	if nonzero_row < 0:
		return False
	if nonzero_row != r:
		swap_rows(matrix, right, nonzero_row, r)
	return True
		
#make_nonzero_base(matrix, 1)
#print(matrix)
#exit()

# return False for infinite solutions
def rid_of_col(matrix, right, r, c):
	if not make_nonzero_base(matrix, right, r, c):
		return False
	base = matrix[r][c]
	for row in range(r + 1, len(matrix)):
		mul = matrix[row][c] / base
		for col in range(c, len(matrix[row])):
			matrix[row][col] = matrix[row][col] - matrix[r][col] * mul
		right[row] = right[row] - right[r] * mul
	return True


# return for infinite solutions
def make_triangle(matrix, cols, right):	
	row = 0
	for n in range(0, cols):
		print(stringify_matrix(matrix, right, 2))
		print('rid of ' + str(n))
		if rid_of_col(matrix, right, row, n):
			row = row + 1
		#print(stringify_matrix(matrix, right, 2))
		#print('----------------------')
	#print(matrix)
	
def rid_of_tail_zeros(matrix, cols, right):
	for row in range(len(matrix) - 1, -1, -1):
		if matrix[row][cols - 1] != 0:
			return True
		if right[row] != 0:
			return False
		del matrix[row]
		del right[row]
	return False
	
def solve(matrix, cols, right):
	make_triangle(matrix, cols, right)
	print(stringify_matrix(matrix, right, 2))
	ok = rid_of_tail_zeros(matrix, cols, right)
	if not ok:
		return 0 # no solutions
	if len(matrix) > cols:
		return 0 # no solutions, duplicates previous check
	if len(matrix) < cols:
		return -1 # infinite solutions
	x = cols * [0]
	
	def calc_x(row, right, n):
		r = right
		for c in range(n + 1, len(row)):
			r = r - row[c] * x[c]
		k = row[n]
		return r / k
		
	for r in range(len(matrix) - 1, -1, -1):
		x[r] = calc_x(matrix[r], right[r], r)
	
	return x # single solution
	
print(stringify_matrix(matrix, right, 2))
print(solve(matrix, cols, right))
print(stringify_matrix(matrix, right, 2))
exit()

		
if fail:
	print('NO')
	exit()

print(matrix)
print(right)
exit()

x = cols * [0]
for row in range(rows - 1, -1, -1):
	num = right[row]
	for row in range(col, -1, -1):
		num = num - 1##############

		x[col] = 1#############333
		

print(x)