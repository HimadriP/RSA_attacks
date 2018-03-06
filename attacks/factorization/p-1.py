def gcd(a,b):
    if a<=0:
        return b
    return gcd(b%a,a)

#The p-1 Method
def factorize(n,B_power):
	a = 2;
	for m in range(2,B_power):
		a = a**m % n
	
	factor = gcd(a-1,n);

        #Check if prime number is obtained
	if 1 < factor  and  factor < n: 
            return factor;
	else: 
            return -1;

def pollard(n):	
	print "Pollard's p-1 factoring"
	print "The value of n is %i" % (n)

        #Initializing the values
	B_power = 2
	d = -1

        #Iterating to get a value of m
	while B_power < n and d == -1:
		B_power +=1
		d = factorize(n,B_power)
	if d == -1: 
            print "N is a prime number"
        else: 
            q = n/d
            print "The Factors are : %i and %i" % (d,q)

n = input("Enter the value of n: ")
pollard(n)
