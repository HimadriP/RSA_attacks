
def legendre_symbol(a,p):
    ''' Returns the Euler's Criterion :
    Checks whether integer is a quadratic residue modulo a prime
    '''
    return pow(a,(p-1)//2,p)


#a=legendre_symbol(5,31)
#print(a)


def tonelli_shanks(n,p):
    ''' To find square roots of a modulo prime '''

    #Base Cases
    if n == 0:
        return [0]

    if p == 2:
        return [n]

    #Check for existence of roots
    if legendre_symbol(n,p) != 1:
        return []

    #Since p-1 = q*2^s
    q = p-1
    s=0
    
    while q%2==0:
        q = q//2
        s = s+1

    if s == 1:
        r = pow(n, (p + 1) // 4, p)
        return [r,p-r]
        
    #Obtaining a non-residue z
    for z in range(1,p-1):
        if p - 1 == legendre_symbol(z, p):
            break

    #Initializing Loop parameters
    c = pow(z,q,p)
    m = s
    t = pow(n,q,p)
    r = pow(n,(q+1)//2,p)

    #print(n,z,c,m,p)    
    
    #Repeat until t is 2^0th root of 1 i.e. t = 1
    while (t-1)%p != 0:

        for i in range(1,m):
            if pow(t,2**i,p) == 1:
                break

        #print(n,c,m,i,p)
        #print(2**(m-i-1))
        #print(1<<(m - i - 1))
        b = pow(c,2**(m-i-1),p)
        m = i
        c = (b * b) % p
        t = (t * b * b) % p
        r = (r * b) % p
        

    return [r,p-r]
    
#ans = tonelli_shanks(15347,17)
#print(ans)
