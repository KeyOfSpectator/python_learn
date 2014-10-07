#advance6.py

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

print lazy_sum()

f = lazy_sum(1,3,5,7,9)
print f()

f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)

print f1 == f2

#test
#point
def test_map(fun,args):
	elem1 = 0
	#print elem1
	#print args
	for elem in args:
		#print elem1
		elem1 = fun(elem,elem1)
	return elem1

#test failed
def lazy_sum_test(x,y):
	def sum_test():
		return x+y
	return sum_test

#test right
def sum_test2(x,y):
	return x+y

print test_map(sum_test2,[1,2,3,4])