def ex_euc_alg(a,b):
    if a==0:
       	return (b,0,1)
    else:
       	g,x,y=ex_euc_alg(b%a,a)
       	return (g,y-(b//a)*x,x)

print ex_euc_alg(8125815438165277351481140933197233052027313307864886671229139569349729,90143305010218464651239068244550223)
