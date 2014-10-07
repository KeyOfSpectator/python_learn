#fun1.py

def my_abs(x):
	if x>=0:
		return x
	else:
		return -x

print my_abs(100)
print my_abs(-100)

def nope(x):
	if x>=0:
		pass
	else:
		return x

print nope(10)

def check_input_nope(x):
	if not isinstance(x,(int, float)):
		raise TypeErro('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print check_input_nope(1)
#print check_input_nope('text')

def multi_intput_return(x,y):
	return x,y
print multi_intput_return(10,20)

#def default_input_power(x=1,y):
def default_input_power(x,y=2):
	sum = x
	while y>0:
		y = y-1
		sum = sum*x
	return sum
print default_input_power(3)
print default_input_power(3,3)

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc([1,2,3])
print calc((1,2,3,4))

def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc2(1,2,3)
print calc2(1,2,3,4) 