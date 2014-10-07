#fun3.py

def fact_common(n):
	sum = n
	while n>1:
		n = n-1
		sum = sum*n
	print sum

fact_common(3)

def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)

print fact(3)
print fact(100)

#print fact(1000)

def fact_iter(product , count , max):
	if count>max:
		return product
	return fact_iter(product * count , count + 1 , max)

def fact_3(n):
	return fact_iter(1,1,n)

print fact_3(5)

#http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00137473836826348026db722d9435483fa38c137b7e685000