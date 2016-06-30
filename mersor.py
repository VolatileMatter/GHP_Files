import random

test2 = [1,9,3,4,5,6,7,8,2]

def in_order(a_list):
	last_item = None
	for item in a_list:
		if not last_item: 
			last_item = item
		if item < last_item:
			return False
		last_item = item
	return True

#Merge Sort. Start with a bunch of singular numbers. combine them in order. As you get larger, eventually you'll have two perfectly sorted arrays. Like a reverse bubble sort?
#Helper method to split an array in half
def merge_sort(aList):
	i=0
	left = []
	right = aList
	if len(aList) == 1:
		return aList
	else: 	
		while i < len(aList):
			left.append(aList[i])
			right.remove(aList[i])
			i+=1
		left = merge_sort(left)
		right = merge_sort(right)
	return merger(left, right)

def order(a,b):
	smLi = [a,b]	
	if smLi[0] > smLi[1]:
		temp1 = smLi[0]
		smLi.remove(temp1)
		smLi.insert(1,temp1)
	return smLi

def merger(lista, listb):
	merged = []
	i = 0
	while i < len(test2):
		merged.append(order(lista[i],listb[i]))
	return merged

def main():
	print merge_sort(test2)
	

	

main()
