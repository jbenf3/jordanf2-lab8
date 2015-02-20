# Your Name
# Physics 91SI, Spring 2013
# Lab 8


#This is a Set class definition in Python

class Set():
	"""This is a Set class.  Basic Set operations include..."""

	def __init__(self):
		self.members = []


	def add(self, val):
		#add your code here
		pass


	def remove(self, val):
		#add your code here
		pass


	def contains(self, val):
		#add your code here
		pass


	def size(self):
		#add your code here
		pass



	def union(self, otherSet):
		#add your code here
		pass



	def intersect(self, otherSet):
		#add your code here
		pass



	def subtract(self, otherSet):
		#add your code here
		pass



	#The following methods are operator overloading methods
	#They need not be separated from the regular methods
	#but are here for simplicity


	def __contains__(self, val):
		#This overloads how the "in" operator works
		#E.g.: x_val in MySet should return True or False
		#add your code here
		pass



	def  __len__(self):
		#This overloads how len(MySet) works
		#len(MySet) should return the same as MySet.size()
		#add your code here
		pass



	def __or__(self, otherSet):
		#This overloads how the "|" operator works
		#E.g.: SetA | SetB should return their union
		#which is what elements are in SetA or SetB
		#For the implementation here, self represents SetA
		#and otherSet represents SetB
		#add your code here
		pass


	def __and__(self, otherSet):
		#This overloads how the "&" operator works
		#E.g.: SetA & SetB should return their intersection
		#which is what elements are in SetA and SetB
		#add your code here
		pass


	def __sub__(self, otherSet):
		#This overloads how the "-" operator works
		#E.g.: SetA - SetB should return their difference
		#which is what elements are in SetA but not in SetB
		#add your code here
		pass


	#The following is definitions for an iterator of 
	#our Set class.  The important points to note is
	#that __iter__ must return self, and there must 
	#be a next() method defined that returns the next
	#member and raises the appropriate exception when
	#the iterator should stop


	def __iter__(self):
		#This overloads how looping over a Set works
		#E.g.: for value in SetA: should work properly
		self.index = len(self.members)
		return self


	def next(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.members[self.index]
