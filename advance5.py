#advance5.py

print sorted([1,2,3,5,4])

def reversed_cmp(x,y):
	if x>y:
		return -1
	if x<y:
		return 1
	return 0

print sorted([1,2,3,5,4],reversed_cmp)

print sorted(['abc','Deg','Zerg','prod'])

def ignore_care_cmp(s1,s2):
	u1 = s1.upper()
	u2 = s2.upper()
	print u1,u2
	if u1>u2:
		return 1
	if u1<u2:
		return -1 
	return 0

print sorted(['abc','Deg','Zerg','prod'],ignore_care_cmp)