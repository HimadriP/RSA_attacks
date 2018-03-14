#from sage.all import *
import math

print "This is used to solve the Discrete Logarithm Problem DLP"
print "If y = a^x mod n, we find x given y,a and n"

y=raw_input("Enter y:")
a=raw_input("Enter a:")
n=raw_input("Enter n:")

#forming groups G 
g1=[]
g2=[]

s=math.floor(math.sqrt(float(n)))
s=int(s)
a=int(a)
y=int(y)
n=int(n)

for p in range(0,s):
    temp=y*(a^p) 
    val=temp%n
    g1.append(val)
 
for q in range(1,s+1):
    temp=a^(q*s) 
    val=temp%n
    g2.append(val)
 
# print "The groups are:"
# print g1
# print g2
 
x1,x2 =0,0
  
for p in g1:
    for q in g2:
        if p==q:
            x1=g1.index(p)            
            x2=g2.index(q)
            print x1,x2
            break
             
result= ((x2+1)*s - x1) % n 
print 'The value of public exponent x is:', result