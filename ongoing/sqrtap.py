import math

n=51923
#a=379
#b=137

def sieve(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    primes = []
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            primes.append(p)
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1

    return primes

n_sqrt = math.sqrt(n)

prime = sieve(int(n_sqrt))
for p in range(2, int(n_sqrt)):
    if prime[p]:
        print p,
        
def factorize(n,steps,rlim,prime):
    epsilon = 0.02
    r=2
    steps = 0

    fx = n_sqrt - math.floor(n_sqrt)
    
    while True:
        while(r<rlim and ( (fx*r != math.floor(fx*r) + epsilon) or (fx*r != math.floor(fx*r) - epsilon))):
            steps = steps + 1
            
              
    
