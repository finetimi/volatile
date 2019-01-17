from functools import reduce


def factorial(num):
	if num == 0:
		return 1
	factorial = reduce(lambda x, y: x * y, reversed(range(1, num + 1)))
	print(factorial)


'''
Integral number
'''
ints = {i: i * i for i in range(1, 8 + 1)}


def run_input():
	import math
	vals = input('Enter a comma separated value of numbers')
	split_vals = vals.split(',')
	map(math.sqrt)


def order_and_sort():
	val = "hello world and practice makes perfect and hello world again"
	newval = list(set(val.split(' ')))
	newval.sort()
	print(' '.join(newval))


def gen_7(n):
	vals = (x for x in range(0, n) if x % 7 == 0)
	print(list(vals))


if __name__ == "__main__":
	gen_7(100)
