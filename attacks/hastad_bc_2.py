import gmpy



def mul_inv(t,n):
    #t*r mod n = 1
    return gmpy.invert(t,n)



def ext_euc_alg(a,b):
    x,x1 = 1,0
    y,y1 = 0,1
    g,g1 = a,b
    while g1:
        q=g//g1
        x=x1
        x1=x- q*x1
        y=y1 
        y1=y- q*y1
        g=g1
        g1=g- q*g1
    return x,y



def CRT(ns, cs):
    #ns : array of Ns
    #cs : array of C
    l = len(ns)
    if not l == len(cs):
        print "Equal number of elements should be there in the arrays"
        return None

    v = 1
    i = 1
    product = 1 
    #sol : sol mod ns[i] = cs[i]. This is the solution of the CRT
    sol = 0
    for i in range(l): 
        product = product*ns[i]
    
    for i in range(l):
        v=product // ns[i]
        sol=sol + (cs[i] * mul_inv(v, ns[i]) * v)

    result=sol%product
    
    return result


#main driver part

ns = [945849313*890855617,142594211*353521913,41692333*775305163]
e = 3
m1 = raw_input("Enter message to be broadcasted:")
m2 = m1#raw_input("Enter mesg2:")
m3 = m1#raw_input("Enter mesg3:")

m1= int(m1.encode("hex"),16)
m2= int(m2.encode("hex"),16)
m3= int(m3.encode("hex"),16)

print "The message is :",m1
#print m2
#print m3 

cs = []
cs.append(pow(m1,e,ns[0]))
print cs[0]
cs.append(pow(m2,e,ns[1]))
print cs[1]
cs.append(pow(m3,e,ns[2]))
print cs[2]

s = CRT(ns, cs)
print s
pt, perfect = gmpy.root(s, e)
m = hex(pt)
b=m[2:].decode("hex")
print "The message is %d or %s" % (pt, hex(pt)) 
print "Text : %s" % b
