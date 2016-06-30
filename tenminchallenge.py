

def bubbleSort(arrayme):
	i = 0
	ans = ""
	while(i<(len(arrayme)-1)):
		temp = arrayme[i]
		temp2 = arrayme[i+1]
		if temp < temp2:
			ans+= str(temp) + ""
			ans+= str(temp2) + ""
		else: 
			ans+= arrayme[i+1]
		print "bub run: "+str(i)+", temp: "+temp+", temp2: "+temp2+", arrayme: "+arrayme+", ans: "+str(ans)
		i+= 1
	print "Ans: "+ans	
	return ans

def isInOrder(arrayme):
	i = 0
	ordered = True
	first = arrayme[0]
	while(i< (len(arrayme)-1)):
		if arrayme[i] < first:
			ordered = false
		i+= 1			
	return ordered

def in_order(num_list):
	last_item = None
	for item in num_list:
		if not last_item: 
			last_item = item
		if item < last_item:
			return False
		last_item = item
	return True


def main():
	AR1 = "42" #yes
	AR2 = "312" #no
	AR3 = "154326" #yes
	print in_order(bubbleSort(AR2))

main()
