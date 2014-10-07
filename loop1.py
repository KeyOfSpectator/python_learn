#loop1.py

class1 = ('elem1','elem2','elem3')

for name in class1:
	print name

sum = 1
for x in [1,2,3,4,5,6]:
	sum = sum + x
print sum

print range(5)


sum = 0
for x in range(101):
	sum = sum + x
print sum

sum = 0
n = 100
while n>0:
	sum = sum + n
	n = n - 1
print sum

#sum = 0
input_n = int(raw_input('input a int between 1 ~ 100 :  '))
if 0<input_n<100:

	while input_n<=100:
		print input_n
		input_n = input_n+1
else:
	print 'input error'
