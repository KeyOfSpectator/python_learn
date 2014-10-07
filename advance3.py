#advance3.py

print range(1,11)

print [x*x for x in range(1,11)]

print [x*x for x in range(1,11) if x%2 == 0]

print [m+n for m in 'ABC' for n in 'XYZ']

L = [x*x for x in range(1,11)]

print L

G = (x*x for x in range(10))

print G

for i in range(10):
	print G.next()