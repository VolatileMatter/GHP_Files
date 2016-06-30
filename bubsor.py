import random

def in_order(a_list):
	last_item = None
	for item in a_list:
		if not last_item: 
			last_item = item
		if item < last_item:
			return False
		last_item = item
	return True

def bubbleSort(a_list):
	i = 0
	temp1 = -1
	temp2 = -1 
	while i < len(a_list) - 1:
		if a_list[i] > a_list[i+1]:
			temp1 = a_list[i]
			a_list.remove(temp1)
			a_list.insert(i+1,temp1)
		i+= 1
	if not in_order(a_list):
		bubbleSort(a_list)
	return a_list


#Everything below here are just lists to test the code with
print ""

mylist = [2,5,1,8,3,9]
test1 = [1,2,3,4,5,6,7,8]
test2 = [1,9,3,4,5,6,7,8,2]
test3 = [4,3,2,1,7,9,8]
test4 = [6,9,10,5,2,8]

print "bubbleSort: "
print bubbleSort(mylist)
print bubbleSort(test1)
print bubbleSort(test2)
print bubbleSort(test3)
print bubbleSort(test4)

print ""

#print "Random list:",ranList
ranList = random.sample(xrange(1, 101), 10)
print bubbleSort(ranList)
ranList = random.sample(xrange(1, 101), 11)
print bubbleSort(ranList)
ranList = random.sample(xrange(1, 101), 12)
print bubbleSort(ranList)
ranList = random.sample(xrange(1, 101), 13)
print bubbleSort(ranList)
ranList = random.sample(xrange(1, 101), 14)
print bubbleSort(ranList)
