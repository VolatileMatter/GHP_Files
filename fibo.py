

def main(repeat):
	start = 0
	n = repeat	
	i = 0
	print fib(n)

def fib(n):
	if(n>1):
		return fib(n-2) + fib(n-1)
	elif n == 0:
		return n
	elif n == 1:
		return n+1

main(6)
	

#def fib(num):
#	if num == 0:
#		return 0
#	elif num == 1:
#		return 1
