#fun2.py

def fun(a,b,c=0,*args,**kw):
	print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw


fun(1,2)

fun(1,2,3)

fun(1,2,3,'a','b',123)

fun(1,2,3,('a','b',123))

fun(1,2,3,'a','b',x=99)