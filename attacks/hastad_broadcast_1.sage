from sage.all import *
import sys

errors=[]

def chinese_remainder(n, a):
    return CRT_list([c1,c2,c3],[n1,n2,n3])
    #sum = 0
    #prod = reduce(lambda a, b: a*b, n)
 
#    for n_i, a_i in zip(n, a):
 #       p = prod / n_i
  #      print p,n_i
   #     print "mulinv" + mul_inv(p,n_i)
    #    sum += a_i * mul_inv(p, n_i) * p
    #return sum % prod 


def ex_euc_alg(a,b):
    if a==0:
       	return (b,0,1)
    else:
       	g,x,y=ex_euc_alg(b%a,a)
       	return (g,y-(b//a)*x,x)    
    
def mul_inv(a, b):
    g, x, _ = ex_euc_alg(a, b)
    if g == 1:
        return x % b


n1=6463622691511358246253843530346957637373771131900115657628956890377133584685693433311356736502535188960628243319843637208561654754340837455923813904935726098046519705940214576082103284466503159415461203969573801791920631195293206011011844763565055300642230449750811779501261575835745322674349086755143
e1=3
n2=8510037142847030608778231217636478160093221085470322047695805385472839268389474788835516797851509710116067378544281194029549685630115441064125513663237564088997109745111221590482125652917053055227873501767060274190671556099364882664979774616818879661100982508212710118592283619809629333761875639670531
e2=3
n3=4904210278926969382082557520192836447620667943738476959012915263821924765704042320598156081670263969687760089856706802802004650936382508871994891329330913843525685058082515207132945533244603569727806893994293885384278666942443580662358108073773755355586360506572438622134010593933877119286516365700963
e3=3



# if(e1!=e2 or e2!=e3):
# 	globals()['errors'].append("e values are not the same")
				
e=e1

m = raw_input("Enter string: ")
m=int(m.encode("hex"),16)

c1 = pow(m,e1,n1)
c2 = pow(m,e2,n2)
c3 = pow(m,e3,n3)

# if(gcd(n1,n2)!=1 or gcd(n2,n3)!=1 or gcd(n1,n3)!=1):
# globals()['errors'].append("The three public moduli are not coprime. Hence hastad attack not possible")
					#As gcd(n1,n2,n3)=1 and m^3 < n1*n2*n3, CRT can be applied to find m^3
#m_cubed=chinese_remainder([c1,c2,c3],[n1,n2,n3])
					# print "M^3 is ",m_cubed

m_cubed = CRT_list([c1,c2,c3],[n1,n2,n3])

f=x**3-m_cubed
roots=f.roots(multiplicities=False,ring=IntegerRing())
					# print "The message is ",roots[0]
#if(len(roots) == 0):
#	globals()['errors'].append('No solution found')

print "The message is %d" % roots



# if __name__ == '__main__':
# 	a=simple_hastad()
# 	print a
