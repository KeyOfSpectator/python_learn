#advanced7.py

#anony function
print map(lambda x: x*x , [1,2,3,4,5,6,7,8,9])

f = lambda x: x+10
print f(1)

def build(x,y):
	return lambda : x+y

#? parameter?? :

f2 = build(1,2)
print f2()