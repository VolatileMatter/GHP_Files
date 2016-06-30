AR1 = [4,2]
AR2 = [3,1,2]
AR3 = [1,5,4,3,2,6]
AR = []

def in_order(num_list):
	last_item = None
	for item in num_list:
		if not last_item: 
			last_item = item
		if item < last_item:
			return False
		last_item = item
	return True

def reverse(num_list): 
	for y in range(num_list): 
		temp_list = num_list
		temp = num_list[x]
		temp_list[x] = temp_list[y]
		temp_list[y] = temp
		if in_order(temp_list):
			return True
