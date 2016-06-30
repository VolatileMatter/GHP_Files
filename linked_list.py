class Node(object): 
	def __init__(self,data=None,next=None,prev=None):
		self.data = data
		self.next = next
		self.prev = prev
		
	def __str__(self):
		ans = "Data:",self.data," Next:",self.next," Prev:",self.prev
		return str(ans)
	def __repr__(self):
		return str(self.data)

	def get_data(self):
		return self.data
	def get_next(self):
		return self.next
	def get_prev(self):
		return self.prev

	def giveData(self, inf):
		self.data = inf
	def giveNext(self, nes):
		self.next = nes
	def givePrev(self, prev):
		self.prev = prev

class LinkedList(object):
	def __init__(self,head=Node(),tail=Node()):
		self.head = head
		self.tail = tail
		self.size = 0
	def __str__(self):
		data = "Head:",self.head," Tail:",self.tail," Size:",self.size
		return str(data)

	def add(self, to_add):
		if self.size == 0:
			self.head = to_add
			self.head.giveNext(to_add)
			self.tail = to_add	
			self.tail.givePrev(to_add)
			#print "Add head:",self.head
			#print "Add tail:",self.tail
		else:		
			temp = self.tail
			temp.giveNext(to_add)
			#print "Add temp:",temp		
			self.tail = to_add
			self.tail.givePrev(temp)
			#print "Add else:", self.tail
		self.size += 1
		#print self.tail
		#print self.head

	def rmv(self):
		#print self.tail
		nwtal = self.tail.get_prev()		
		self.tail.prev = None
		self.tail = nwtal
		self.size -= 1
	
	def addB4(self, toAdd, addB4):
		if self.toAdd.getData() == addB4.getData():
			


#if size = 0 then whatever you add will become the head.
#If it's only one long, make everything reference itself. 

atl = Node("Atlanta")
sav = Node("Savannah")
ptc = Node("PeachTree")
fst = Node("Forsyth")
mcn = Node("Macon")
vda = Node("Valdosta")

nll = LinkedList()

#dog = Node()
#print dog
#dog.giveData("Bark bark!")
#print dog
#dog.givePrev(atl)
#print dog
#dog.giveNext(ptc)
#print dog

nll.add(ptc)
nll.add(atl)
nll.add(fst)
nll.rmv()
nll.rmv()
nll.add(sav)

print nll
