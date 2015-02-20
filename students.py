#!/usr/bin/env python

# Your Name
# Physics 91SI, Spring 2013
# Lab 8

class Student:
    """Docstring for Student class"""


#self is analogous to this from java and c++
#all of these self inclusions are necessary
    def __init__(self, name):
        """Takes one arg, string which holds the name of the Student"""

        self.name = name
#there are no private variables in python, but its common practice to
#denote variable that should be private/left alone by the client 
#by naming them as so, self._name

        self.units = 0
        self.courses = []
    
    def get_name(self):
        return self.name

    def add_units(self, units):
        self.units += units

    def get_units(self):
        return self.units

    def can_graduate(self):
        return (self.units >= 180)

    def add_course(self, course):
        self.course.append(course)

    def print_courses(self):
        print self.courses

    def __len__(self):
        return self.units

    def __eq__(self, other):
        #Simple equality test just checks if names match
        return self.name == other.name

class GradStudent(Student): 
#this is how you create a subclass that extends the Student class
    def __init__(self, name):
        Student.__init__(self,name)
        self.thesisdone = False

    def complete_thesis():
        self.thesisdone = True

    def can_graduate(self):
        return (self.units >= 45) and self.thesisdone
