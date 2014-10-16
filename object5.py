#object5.py

class Student(object):
	def __init__(self,name,score):
		self.score = score
		self.name = name
	def print_stu(self):
		print "%s : %s" % (self.name,self.score)

ming = Student('ming',21)
ming.print_stu()

print hasattr(ming , 'score')

print hasattr(ming , 'sex')

setattr(ming , 'sex' , 'male')

print hasattr(ming , 'sex')

print ming.sex

print getattr(ming, 'sex')

#error
#print getattr(ming, 'level')

#
print getattr(ming, 'level' , 'default_str')

print hasattr(ming , 'print_stu')

print getattr(ming , 'print_stu')

fn = getattr(ming , 'print_stu')

fn()