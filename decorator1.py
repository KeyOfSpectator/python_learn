#decorator1.py

def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print '%s %s():' %(text, func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print '2014-10-9'

now()

print now.__name__