# Fast python code that first calls pow() 
# then applies % operator
a = 2
b = 100
p = (int)(1e9+7)
 
# Using direct fast method to compute 
# (a ^ b) % p.
d = pow(a, b, p)
print d
