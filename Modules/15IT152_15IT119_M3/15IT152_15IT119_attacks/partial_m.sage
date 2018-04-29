
import time
from Crypto.Util.number import bytes_to_long, long_to_bytes 

debug = False


# This displays the matrix 

def view_matrix(BB, bound):
    
    for ii in range(BB.dimensions()[0]):
        
        a = ('%02d ' % ii)
        
        for jj in range(BB.dimensions()[1]):
            
            a += '0' if BB[ii,jj] == 0 else 'X'
            
            a += ' '
        
        if BB[ii, ii] >= bound:
            a += '~'
        print a

def coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX):
    
    dd = pol.degree()
    nn = dd * mm + tt

    #ring of pol and x is changed here
    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    #here we compute the polynomials according to howgrave univariate
    gg = []
    
    for ii in range(mm):
        
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)
    
    
    #construction of lattice B
    
    B = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            B[ii, jj] = gg[ii][jj]

    #view the matrix
    
    if debug:
        view_matrix(B, modulus^mm)

    #Using LLL algorithm
    B=B.LLL()

    #transform shortest vector in polynomial    
    
    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii*B[0, ii] / XX**ii

    #factoring the polynomial
    possible_r= new_pol.roots()
    print "The possible roots from Coppersmith Howgrave Algorithm are:", possible_r

    #testing the correctness of the roots
    roots = []
    for root in possible_r:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

	return roots


def partial_message_exposure(input):
    
    N = input['N']
    e = input['e']
    C = input['C']
    K = input['known_plaintext']
    
    ZmodN = Zmod(N)
    P.<x> = PolynomialRing(ZmodN) 
    pol   = (K+x)^e - C 
    dd    = pol.degree()
    
    beta  = 1.0
    epsilon = beta/7
    
    mm = ceil(beta**2/(dd*epsilon))
    tt = floor(dd * mm * ((1/beta) - 1))
    XX = ceil(N**((beta**2/dd)-epsilon))
    
    root_set=coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)
    solution = {};
    solution['roots'] = root_set
    solution['error']  = 'None'
    if(len(root_set)==0):
    	result['error'] = 'No solution found'
	return solution


print "DEMO INPUTS:"

kp=raw_input("Enter the known plaintext KP:")
print ""

length_N = 1024  # size of the modulus
Kbits = 200      # size of the root
e = 3

p = next_prime(2^int(round(length_N/2)))
q = next_prime(p)
N = p*q
ZmodN = Zmod(N)
print "Value of N for the demo is", N
print ""
print "Value of e for the demo is", e
print ""


K = Integer(bytes_to_long(kp))

Kdigits = K.digits(2)

#making the message
M = [0]*Kbits + [1]*(length_N-Kbits); 

for i in range(len(Kdigits)):
    M[i] = Kdigits[i]

M = ZZ(M, 2) #message completed

#corresponding ciphertext
C = ZmodN(M)^e

known=2^length_N - 2^Kbits

print "The value of M is:", M
print "The value of C is:", C

input={}
input['N'] = N
input['e'] = e
input['known_plaintext'] = known
input['C'] = C
#print input 
results = partial_message_exposure(input)
print "The possible values for the rest of the message is:"
print results



