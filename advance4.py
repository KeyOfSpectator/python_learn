#advance4.py

def f(x):
	return x*x

print map(f,[1,2,3,4])

def f2(x1,x2):
	return x1+x2

print reduce(f2,[1,2,3,4,5])

def fn(x,y):
	return x*10+y

print reduce(fn,[1,2,3,4,5])

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print char2num('1')	

print map(char2num,'12345')

print reduce(fn,map(char2num,'152345'))

def char2int(s):
	return reduce(fn,map(char2num,s))

print char2int('9876554321')