#object_advance1.py

class Student(object):
	pass

s = Student()
s.name = 'Yang'
print s.name

# add func to instance
def set_age(self,age):
	self.age = age

#
from types import MethodType
s.set_age = MethodType(set_age , s , Student)
s.set_age(25)
print s.age

s2 = Student()
# the other instance is not work
#s2.set_age(23)


#add func to class
def set_score(self,score):
	self.score = score

Student.set_score = MethodType(set_score , None , Student)

s.set_score(100)
print s.score

s2.set_score(99)
print s2.score