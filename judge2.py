#judge2.py

age = raw_input()
age = int(age)
print age
if age <= 18:
	print 'you are teenager'
	print "you are young"
	print age
elif age < 100:
	print "you are still young"
	print age
elif age < 1000:
	print "you maybe god"
	print age
else:
	print "you are god"
	print age