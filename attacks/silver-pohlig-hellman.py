
import math
import time

def RP(x,y,z):
    s = 1;
    while(x>0):
        if(x%2==1):
            s=(s*y)%z;        
        x=x//2;
        y=(y*y)%z;            
    return int(s);
                        
def egcd(a, b):
    u1=1;
    v1=0;
    u2=0; 
    v2=1;
    while(b>0):        
        r=a%b
        q=a//b               
        a=b; 
        b=r;
        u1prime = u1
        v1prime = v1
        u2prime = u2
        v2prime = v2        
        u1=u2;
        v1=v2;        
        u2=(u1prime - (u2prime * q));
        v2=  (v1prime - (v2prime * q));
    return u1, v1;


def isPrime(y):
    h = 2;
    while h <= math.ceil(y/2):
        if y % h == 0:
            return 0;
        h += 1;
    return 1 


def computeM (p):
    m = math.ceil(math.sqrt(p-1));
    return m;

def factors(F): 
    X = [];    
    while(F != []):
        X.append((F[0],F.count(F[0])));
        F=F[F.count(F[0]):len(F)];
    return X;

def silverPohligHellman(P, a, b, n):
    A = [];
    u = 0;
    (aInv, _) = egcd(a, n);
    aInv = aInv % n;
    c = n-1;
    r = b; 
    for i in range(0, len(P)): 
        x = RP((c/(P[i][0])), a, n);
        
        for j in range(0, (P[i][1])):                                  
            
            y=RP((c/((P[i][0])**(j+1))), b, n);
            
            for k in range(0, (P[i][0])): 
                
                if pow(x, k, n) == y:
                    u += k*(P[i][0]**j);
                    break;           
            
            b=(b*RP((P[i][0]**j)*k,aInv,n)) % n;
        A.append(u);
        u = 0;
        b = r;                 
    return A; 

def compute(X, P):
   x = 0;
   N = 1;
   Y = [];
   for k in range(0, len(P)):
       Y.append(P[k][0]**P[k][1]);
   for j in range(0, len(Y)):
       N *= Y[j];
   for i in range(0, len(Y)):
       (s, _) = egcd(int(N/Y[i]), Y[i]);    
       e = s*(int(N/Y[i])); 
       x += X[i]*e; 
   return x; 

def factor(x, primeFactors, i):
    j = 2; 
    if x == 1:
        return;
    else:
        while j<math.ceil(x/2): 
            if(x%j)==0:  
                if isPrime(j): 
                    primeFactors.append(j);
                    if isPrime(x/j): 
                        primeFactors.append(x/j);
                        return;
                    else:
                        i+=1;
                        factor((x/primeFactors[(i-1)]),primeFactors,i);  
                        return;
            j += 1;
    return
    

F = [];
print "Solving DLP for a^x=b mod n"
print "Enter a: ";
a = int(raw_input());
print "Enter b: ";
b = int(raw_input());    
print "Enter n(n should have small prime factors):";
n = int(raw_input()); 
factor(n-1, F, 0); 
F = factors(F); #power of the prime factor
Z = silverPohligHellman(F, a, b, n);
x = compute(Z, F);
if(x<0):
    x=x+(n-1)
print "x = " + str(x);
    

