#!/usr/bin/env python


#object_advance6.py
class Animal(object):
    pass


class Runnable(Animal):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Dog(Runnable , Flyable):
	pass

dog = Dog()

dog.run()

dog.fly()