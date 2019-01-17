
arr = [2, 8, 4, 5, 6, 7, 9, 3]
'''
Place all variables in an array which are even first.
'''

def even_first(arr):
	next_even = 0
	next_odd = len(arr) - 1
	while next_even < next_odd:
		if arr[next_even] % 2 == 0:
			next_even += 1
		else:
			arr[next_even], arr[next_odd] = arr[next_even], arr[next_even]
			next_odd -= 1
		pass

# def even_first(arr):
# 	'''
# 	How this works is simple we shift each
# 	non even number to the back of the array
# 	'''
# 	'''
# 	Space complexity: 0(1)
# 	Time complexity: 0(n)
# 	'''

# 	next_even, next_odd = 0, len(arr) - 1
# 	while next_even < next_odd:
# 		if arr[next_even] % 2 == 0:
# 			next_even += 1
# 		else:
# 			arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
# 			next_odd -= 1
# 	print(arr)


'''
QUICK SORT
	Sorts the array
'''
def sort_pivot(pivot_index, arr):
	pivot = arr[pivot_index]
	for i in range(len(arr)):
		for ani in range(i + 1, len(arr)):
			if ani < pivot:
				arr[ani], arr[i] = arr[i], arr[ani]
				break
		

if __name__ == '__main__':
	even_first(arr)