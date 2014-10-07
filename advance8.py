#advance8.py
#decorator
'''
def now():
	print '2014-10-9'

f = now
print f()

print now.__name__
print f.__name__

'''

def log(func):
	def wrapper(*args,**kx):
		print 'call %s():'%func.__name__
		return func(*args,**kx)
	return wrapper

@log
def now():
	print '2014-10-9'

now()