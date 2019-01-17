def numbits(x):
	count = 0
	while (x):
		count += x & 1
		x >>= 1
	print(count)
	return count


# def parity(x):
# 	count = 0
# 	while x:
# 		count += x & 1
# 		x 

# def rightmostone(x):
# 	while(x):
# 		x ^ x

if __name__ == '__main__':
	numbits(52)