#from sage.all import *
import math

print "This is used to solve the Discrete Logarithm Problem DLP"
print "If y = a^x mod n, we find x given y,a and n"

y=raw_input("Enter y:")
a=raw_input("Enter a:")
n=raw_input("Enter n:")

#forming groups G 
S=[]
T=[]

s=math.floor(math.sqrt(float(n)))
s=int(s)
a=int(a)
y=int(y)
n=int(n)

print s,a,y,n

for r in range(0,s):
    temp=y*(a**r) 
    val=temp%n
    S.append((val,r))
 
for t in range(1,s+1):
    temp=a**(t*s) 
    val=temp%n
    T.append((val,t*s))
 
print "The groups are:"
print S
print T
 
x1,x2 =0,0
  
for p,r in S:
    for q,ts in T:
        if p==q:
            # x1=S.index(p)            
            # x2=T.index(q)
            # print x1,x2
            # result= ((x2+1)*s - x1) % n
            x=ts-r
            print "The value of x is:", x
             
# result= ((x2+1)*s - x1) % n 
# print 'The value of x is:', result