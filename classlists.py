#ClassList class definition in Python
#Inherits from Set class

# Your Name
# Physics91SI, Spring 2013
# Lab 8

from sets import Set
from students import *

class ClassList(Set):
	"""Docstring for ClassList class"""

	#__init__ should be the same as defined in Set
	#so no need to overwrite it


	def add(self, name):
		#Overwrite the add method so that the user
		#can give a string argument containing the
		#student's name and then your implementation
		#here will create a new Student object
		#and add that to the member list
		pass


	
	def remove(self, name):
		#Similar to above. Allow the user to give a string
		#name and then your implementation should search 
		#the member list for the Student object with a 
		#matching name and remove it
		pass


	def contains(self, name):
		#Same process as both above.
		pass




	#Challenge methods


	#You can overwrite the iterator methods so that it will 
	#run over the Student names in alphabetical order
	def __iter__(self):
		return self

	def next(self):
		pass


	#You can overwrite the slice operator, ie MySet[a : b]
	#Have it work with MyClass["A" : "H"], so that this returns
	#a new ClassList object that only contains students
	#with the last name initial from "A" to "H"
	def __getslice__(self, a, b):
		pass
