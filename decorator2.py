#decorator2.py

import functools

def log1(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call %s (): ' % func.__name__
		return func(*args,**kw)
	return wrapper

@log1
def f1():
	print '2014-10-9 f1'

f1()
print f1.__name__


def log2(text):
	def decorator1(func):

		@functools.wraps(func)
		#!

		def wrapper(*args,**kw):
			print 'text: %s , call %s ():'% (text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator1

@log2('log2 execution')
def f2():
	print '2014-10-9 f2'

f2()
print f2.__name__

###????!!!!