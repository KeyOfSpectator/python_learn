#object3.py

class Student(object):
	def __init__(self,name,elem1,elem2):
		self.name = name
		self.__elem1 = elem1
		self._elem2 = elem2

	def __print_stu(self):
		print "__print_stu"
		print self.name
		print self.__elem1
		print self._elem2

	def print_stu2(self):
		print "print_stu2"
		print self.name
		print self.__elem1
		print self._elem2

	def _print_stu3(self):
		print "_print_stu3"
		print self.name
		print self.__elem1
		print self._elem2

fsc = Student('fsc','e1','e2')

#cant
#fsc.__print_stu()
#print getattr(fsc,'__print_stu()')

fsc.print_stu2()

fsc._print_stu3()

print fsc.name

#cant
#print fsc.__elem1
#print getattr(fsc,'__elem1')
#>_<

print fsc._elem2

