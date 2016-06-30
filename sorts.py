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

#Insertion Sort
def insertionSort(alist):
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index
		while position>0 and alist[position-1]>currentvalue:
			alist[position]=alist[position-1]
			position = position-1
			alist[position]=currentvalue
	return alist

ranList = random.sample(xrange(1, 101), 10)
print "Random list:",ranList
print ""

mylist = [2,5,1,8,3,9]
test1 = [1,2,3,4,5,6,7,8]
test2 = [1,9,3,4,5,6,7,8,2]
test3 = [4,3,2,1,7,9,8]
test4 = [6,9,10,5,2,8]

print "insertion: "
print insertionSort(mylist)
print insertionSort(ranList)

print ""
