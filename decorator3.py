#decorator3.py

def log_test(func):
	def wrapper():
		#no parameter
		print 'this is a test and call %s():' % func.__name__
		return func()
	return wrapper

@log_test
def f1():
	print 'this is the output f1'


f1()