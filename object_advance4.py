#object_advance4.py
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth

s = Student()

s.birth = 1992
print s.birth
print s.age