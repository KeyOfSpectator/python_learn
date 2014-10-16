#object4.py
class Animal(object):
	def run(self):
		print "Animal is running..."

class Dog(Animal):
	def run(self):
		print "dog is running..."

	def __len__(self):
		return 3

class Cat(Animal):
	pass

dog = Dog()
dog.run()

cat = Cat()
cat.run()

class Grandf(object):
	def say(self):
		print "i m grandf"

class Fath(Grandf):
	def say(self):
		print "i m fath"

class Child(Fath):
	def say(self):
		print "i m child"

child = Child()
child.say()

fath = Fath()
fath.say()

grandf = Grandf()
grandf.say()

print isinstance(grandf,Grandf)

print isinstance(child , Fath)
#true

def say_twice(Fath):
	Fath.say()
	Fath.say()

say_twice(child)
#child say

print type(fath)

print type(123) == type(2345)

import types
print type("stringasdf")==types.StringType

#class
print dir(Fath())

#instance
print dir(grandf)

print dog.__len__()
print len(dog)


print '=========='
