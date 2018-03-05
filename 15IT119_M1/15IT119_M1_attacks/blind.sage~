from sage.all import *
from random import random

def rsa(bits):
    # only prove correctness up to 1024 bits
    proof = (bits <= 1024)
    p = next_prime(ZZ.random_element(2**(bits//2+1)), proof=proof)
    q = next_prime(ZZ.random_element(2**(bits//2+1)), proof=proof)
    n = p*q
    phi_n = (p-1)*(q-1)
    while True:
        e = ZZ.random_element(1,phi_n)
        if gcd(e,phi_n) == 1:
            break
    d = lift(Mod(e,phi_n)^(-1))
    return e, d, n


def encrypt(msg,pubkey):
    coded = power_mod(int(msg),pubkey[0],pubkey[1])
    return coded

def decrypt(msg, privkey):
    coded = power_mod(int(msg),privkey[0],privkey[1])
    return coded

def signature(msg, privkey):
    return decrypt(msg,privkey)

def blindingfactor(N):
    r=ZZ.random_element(N)    
    while (gcd(r,N)!=1):
        r=ZZ.random_element(N)
    return r

def blind(msg,pubkey):  
    r=blindingfactor(pubkey[1])
    m=int(msg)
    blindmsg=(pow(r,*pubkey)*m)% pubkey[1]
    #print "Blinded Message "+str(blindmsg)
    return blindmsg,r

def unblind(msg,r,pubkey):
    bsm=int(msg)
    ubsm=(bsm*inverse_mod(r,pubkey[1]))% pubkey[1]
    #print "Unblinded Signed Message "+str(ubsm)
    return ubsm
    
e,d,n = rsa(1024)

pubkey = (e,n)
privkey = (d,n)

msg = raw_input("Enter your message: ")
msg = int(msg.encode("hex"),16)

print "Your encoded message is %d" % msg

#msg = 56789

print ""
signedtrue = signature(msg,privkey)
print "The Signature is %d" % signedtrue

print ""
blindedmsg,r = blind(msg,pubkey)
print "The Blinded Msg is %d" % blindedmsg

print ""
signedbmsg = signature(blindedmsg, privkey)
print "The Signed Blinded Message is %d" % signedbmsg

print ""
unblindsignedmsg = unblind(signedbmsg,r,pubkey)
print "The unblind signed message is %d" % unblindsignedmsg

temp = encrypt(unblindsignedmsg,pubkey)
print ""

m=hex(temp)

m=m.decode("hex")
print "The Msg is " + m
