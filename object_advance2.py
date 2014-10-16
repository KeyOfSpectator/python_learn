#object_advance2.py

class Student(object):
	__slots__ = ('name','age')

s = Student()
s.name = 'Ming'
s.age = 25
#s.score = 99

class GraduateStudent(Student):
	pass

s2 = GraduateStudent()
s2.score = 999
s2.name = 'Yang'
s2.age = 22

print s2.score