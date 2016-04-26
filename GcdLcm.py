def GCD(a,b):
	while(a!=b):
		if(a>b):
			a=a-b
		elif(b>a):
			b=b-a
	return a
def LCM(a,b):
	gcd = GCD(a,b)
	lcm = (a*b)/gcd
	return lcm
print(LCM(3,5))