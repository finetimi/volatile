import time
from random import randint

# def sumOfN(n):
# 	start = time.time()
# 	thesum = 0
# 	for i in range(0, n):
# 		thesum += 1
# 	end = time.time()
# 	print(end - start)
# 	return thesum, end - start

def sumOfN(n):
	start = time.time()
	thesum = (n*(n + 1))/2
	end = time.time()
	print(end - start)
	return end


def find_min(alist):
	overall_min = alist[0]
	for an in alist:
		if overall_min < an:
			overall_min = an
	print(overall_min)


def timelist():
	for listsize in range(1000, 100001, 100):
		start = time.time()
		alist = [randint(1000) for it in listsize]
		end = time.time()


if __name__ == '__main__':
	find_min([5, 6, 3, 4, 10, 1])
