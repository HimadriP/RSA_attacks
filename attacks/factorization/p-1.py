def gcd(a,b):
    if a<=0:
        return b
    return gcd(b%a,a)

def factorize(n,b):
	""" Factor using Pollard's p-1 method """

	a = 2;
	for j in range(2,b):
		a = a**j % n
	
	d = gcd(a-1,n);
	#print "d:",d,"a-1:",a-1
	if 1 < d < n: return d;
	else: return -1;

def pollard(n):
	
	print "Pollard's p-1 factoring"
	
	#n = 13493
	s = 2
	d = -1

	print "n=%i" % (n)

	while s < n and d == -1:
		s +=1
		d = factorize(n,s)
		#print "Round %i = %i" % (s,d)

	if d == -1: print "No Factor could be found ..."
        else: print "%i has a factor of %i, with b=%i" % (n,d,s)

n = input("Enter the value of n: ")
pollard(n)
