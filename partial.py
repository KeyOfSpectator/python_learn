#partial.py

print int('20',base = 8)
#change 8 => 10

print '======================'


import functools
int2 = functools.partial(int ,base = 2)

print int2('1000')

def test_fun(x,y,z):
	print '%s %s %s'% (x,y,z)

test_fun_partial = functools.partial(test_fun , y = 1 , z = 2)

test_fun_partial(5)