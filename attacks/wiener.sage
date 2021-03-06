
#Wiener's Attack is based on continued Fractions

def rsa(bits):
    # only prove correctness up to 1024 bits
    proof = (bits <= 1024)
    p = next_prime(ZZ.random_element(2**(bits//2+1)), proof=proof)
    q = next_prime(ZZ.random_element(2**(bits//2+1)), proof=proof)
    n = p*q
    phi_n = (p-1)*(q-1)
    while True:
        d = ZZ.random_element(2**(bits//4))
	#print(n,36*pow(e,4))
        if gcd(d,phi_n) == 1 and 36*pow(d,4) < n:
            break
    e = lift(Mod(d,phi_n)^(-1))
    return e, d, n

def rational_to_partialquotient(x,y):
    #Making a list of partial Quotients
    a = x//y
    partialq = [a]
    while a * y != x:
        x,y = y,x-a*y
        a = x//y
        partialq.append(a)
    return partialq

def partialquotient_to_rational (frac):
    #From a list of partial quotients to fractions
    if len(frac) == 0:
        return (0,1)

    #x is the numerator
    x = frac[-1]

    #y is the denominator
    y = 1
    
    for _ in range(-2,-len(frac)-1,-1):
        x, y = frac[_]*x+y, x
    return (x,y)

def convergents_from_partialquotient(frac):
    #Given a list of partial quotients - compute convergent
    convs = [];
    for i in range(len(frac)):
        convs.append(partialquotient_to_rational(frac[0:i]))
    return convs

def square_root(n):
    #Calculate the square root
    if n == 0:
        return 0
    a, b = divmod(len(bin(n))-2, 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def check_perf_sqr(n):
    h = n & 0xF; #last hexadecimal digit
    
    if h > 9:
        return -1 

    # Boolean short-circuit - Helps detect false cases quicker
    if ( h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8 ):
        # take square root if you must
        t = square_root(n)
	if t*t == n:
            return t
        else:
            return -1    
    return -1


def wiener_attack(e,n):
    
    frac = rational_to_partialquotient(e, n)
    #print("The continued fractions are : ",frac) 
    convergents = convergents_from_partialquotient(frac)
    #print("The convergents are : ",convergents)

    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:

	    print("\nPreliminary Testcase for d passed...")
            
	    phi = (e*d-1)//k
	    print("\nTemporary value of phi is:",phi)
	    s = n - phi + 1
            # Check if the equation x^2 - s*x + n = 0 has perfect integral roots
            # The integral roots denote the values p and q ( factorization )
            discriminant = s*s - 4*n
            if(discriminant>=0):
		
                t = check_perf_sqr(discriminant)
                if t!=-1 and (s+t)%2==0:
		    print("\nDiscriminant is a perfect square - Roots are integers - p and q. Hence d value is accurate. ")
                    return d

if __name__ == "__main__":
    print("Generating keys ...")
    e,d,n = rsa(1024)

    print("\nThe value of n is %d \n\nThe value of e and d are %d and %d" % (n,e,d))

    print("\nTrying weiner's attack")
    outd = wiener_attack(e, n)
    print("The d from the attack is %d" % outd)
    
    if outd == d:
        print ("\nThe attack worked. The d from the attack matches with our original d generated by the RSA algorithm")
    else:
        print("Attack failed")
