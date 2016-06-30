def fib(num, values):
	fib1 = 0
	fib2 = 0
	if num == 0:
		return 0
	if num == 1:
		return 1
	if num-1 in values:
		fib1 = values[num-1]
	else:
		fib1 = fib(num-1, values)
		values[num-1] = fib1
	if num -2 in values: 
		fib2 = values[num-2]
	else: 
		fib2 = fib(num-2, values)
		values[num-2] = fib2
	return fib1 + fib2
	
if __name__ == '__main__':
	values = {}
	for i in range(50):
		print fib(i, values)
