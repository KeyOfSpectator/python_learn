#object2.py

class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print "%s : %s" % (self.name , self.score)


fsc = Student('fsc',12)

zc = Student('zc',15)

fsc.print_score()
zc.print_score()

def print_object(stu):
	print stu.name
	print stu.score

print_object(fsc)

print fsc.name