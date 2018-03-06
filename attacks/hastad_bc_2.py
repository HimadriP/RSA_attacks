import gmpy

def eGCD(a, b):
    
    #extended euclidean algorithm. g,x,y such that ax+by=g=gcd(a,b)
    
    u, u1 = 1, 0
    v, v1 = 0, 1
    g, g1 = a, b
    while g1:
            q = g // g1
            u, u1 = u1, u - q * u1
            v, v1 = v1, v - q * v1
            g, g1 = g1, g - q * g1
    return u, v

def modInv(a, m):
    
    #r for a*r mod m = 1
    
    return gmpy.invert(a, m)

def CRT(ns, cs):
   
    #Chinese Remainder Theorem
    #ns is the array of moduli
    #cs is the array of C
    #s for s mod ns[i] = cs[i]
    
    length = len(ns)
    if not length == len(cs):
        print "The lengths of the two must be the same"
        return None

    p = i = prod = 1 
    s = 0
    for i in range(length): 
        prod *= ns[i]
    for i in range(length):
        p = prod // ns[i]
        s += cs[i] * modInv(p, ns[i]) * p
    return s % prod


ns = [3,4,5]
e = 3
m1 = raw_input("Enter mesg1:")
m2 = raw_input("Enter mesg2:")
m3 = raw_input("Enter mesg3:")

m1= int(m1.encode("hex"),16)
m2= int(m2.encode("hex"),16)
m3= int(m3.encode("hex"),16)

print m1
print m2
print m3 

cs = []
cs.append(pow(m1,e,ns[0]))
print cs[0]
cs.append(pow(m2,e,ns[1]))
print cs[1]
cs.append(pow(m3,e,ns[2]))
print cs[2]

s = CRT(ns, cs)
pt, perfect = gmpy.root(s, e)
if perfect:
    print "The message is %d or %s" % (pt, hex(pt)) 
else:
    print "Cannot find %dth root of %d" % (e, s)