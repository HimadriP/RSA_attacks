from tonelli_shanks1 import legendre_symbol,tonelli_shanks
from math import sqrt,exp,log,e
from itertools import chain

#Basic GCD 
def gcd(a,b):
    if b<=0:
        return a
    return gcd(b,a%b)

# Newton's method, returns exact int for large squares
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

#Calculating the size of factor base
def calcB(n):
    ln = log(n,e)
    ln_ln = log(ln,e)

    p = sqrt(ln*ln_ln)
    CONSTANT = sqrt(2)/4

    p = p * CONSTANT

    return exp(p)

#Sieve of Eratosthenes
def sieve(n):
    filter = [True] * (n + 1)
    primes = []
    for p in range(2, n + 1):
        if filter[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                filter[i] = False
    return primes

def filter_base(n,B):
    primes = sieve(B)

    factor_base = list()
    for prime in primes:
        if legendre_symbol(n,prime) == 1: factor_base.append(prime)
        
    return factor_base

def smoothness_sieve(factor_base,n,I):

    root_n = int(sqrt(n))
    sieve_sequence = [x**2 - n for x in range(root_n-I,root_n+I)]

    list_sieve = sieve_sequence[:]

    #For simpler case = 2, reducing the factors
    if factor_base[0] == 2:
        i = 0
        while list_sieve[i] % 2 != 0:
            i += 1
        for j in range(i,len(list_sieve),2): # found the 1st even term, now every other term will also be even
            while list_sieve[j] % 2 == 0: #account for powers of 2
                list_sieve[j] //= 2

    #for other primes
    for p in factor_base[1:]:
        #Residues of tonelli shank function -- roots modulo p
        # x such that x^2 = n mod p
        res = tonelli_shanks(n,p)

        for r in res:
            for i in range((r-root_n+I) % p, len(list_sieve), p): # Now every pth term will also be divisible
                while list_sieve[i] % p == 0: #account for prime powers
                    list_sieve[i] //= p
                    
            for i in range(((r-root_n+I) % p)+I, 0, -p): # Going the negative direction!
                while list_sieve[i] % p == 0: #account for prime powers
                    list_sieve[i] //= p
    
    indices = [] # index of discovery
    xlist = [] #original x terms
    smooth_nums = []

    #Tolerance Factor
    T=1
    
    for i in range(len(list_sieve)):
        if len(smooth_nums) >= len(factor_base)+T: #probability of no solutions is 2^-T
            break
        elif list_sieve[i] == 1 or list_sieve[i] == -1: # found B-smooth number
            smooth_nums.append(sieve_sequence[i])
            xlist.append(i+root_n-I)
            indices.append(i)
            
    return (smooth_nums,xlist,indices)
    
def gen_exponent_vectors(smooth_numbers, factor_base):

    #Trial division to split the number into prime powers over the factor_base
    def factorize(n,factor_base):
        factors = []

        if n<0:
            factors.append(-1)

        for p in factor_base:
            if p == -1:
                pass
            else:
                while n % p == 0:
                    factors.append(p)
                    n //= p
        return factors

    Mat = []
    factor_base.insert(0,-1)

    for num in smooth_numbers:
        exp_vector = [0]*(len(factor_base))
        factors = factorize(num, factor_base)

        #print(n,factors)
        for i in range(len(factor_base)):
            if factor_base[i] in factors:
                exp_vector[i] = (exp_vector[i] + factors.count(factor_base[i])) % 2

        #print(n_factors, exp_vector)
        #If congruent sqaure already obtained
        if 1 not in exp_vector: 
            return True, num
        else:
            pass
        
        Mat.append(exp_vector)
        
    #print("Matrix built:")
    #mprint(M)
    return(False, transpose(Mat))

def transpose(matrix):
#transpose matrix so columns become rows, makes list comp easier to work with
    new_mat = []

    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        new_mat.append(new_row)

    return(new_mat)

def gauss_elim(M):
#reduced form of gaussian elimination, finds rref and reads off the nullspace
#https://www.cs.umd.edu/~gasarch/TOPICS/factoring/fastgauss.pdf
    #mprint(M)
    #M = optimize(M)
    marks = [False]*len(M[0])
    
    for i in range(len(M)): #do for all rows
        row = M[i]
        #print(row)
        
        for num in row: #search for pivot
            if num == 1:
                #print("found pivot at column " + str(row.index(num)+1))
                j = row.index(num) # column index
                marks[j] = True
                
                for k in chain(range(0,i),range(i+1,len(M))): #search for other 1s in the same column
                    if M[k][j] == 1:
                        for i in range(len(M[k])):
                            M[k][i] = (M[k][i] + row[i])%2
                break
            
    print(marks)
    M = transpose(M)
    #mprint(M)
    
    sol_rows = []
    for i in range(len(marks)): #find free columns (which have now become rows)
        if marks[i]== False:
            free_row = [M[i],i]
            sol_rows.append(free_row)
    
    if not sol_rows:
        return("No solution found. Need more smooth numbers.")

    print("Found {} potential solutions".format(len(sol_rows)))
    return sol_rows,marks,M

def solve_row(sol_rows,M,marks,K=0):
    solution_vec, indices = [],[]
    free_row = sol_rows[K][0] # may be multiple K
    for i in range(len(free_row)):
        if free_row[i] == 1: 
            indices.append(i)
    
    for r in range(len(M)): #rows with 1 in the same column will be dependent
        for i in indices:
            if M[r][i] == 1 and marks[r]:
                solution_vec.append(r)
                break
            
    print("Found linear dependencies at rows "+ str(solution_vec))     
    solution_vec.append(sol_rows[K][1])       
    return(solution_vec)
    
def solve(solution_vec,smooth_nums,xlist,N):
    
    solution_nums = [smooth_nums[i] for i in solution_vec]
    x_nums = [xlist[i] for i in solution_vec]
    print(solution_nums,x_nums)
    
    Asquare = 1
    for n in solution_nums:
        Asquare *= n
    #print(Asquare)
        
    b = 1
    for n in x_nums:
        b *= n

    a = isqrt(Asquare)
    print(str(a)+"^2 = "+str(b)+"^2 mod "+str(N))
    
    factor = gcd(b-a,N)
    return factor


def quad_sieve(n,B,size_B,I):
    ''' Here n -> Number to be factored
    B -> Smoothness limit
    I -> Sieving Interval'''

    root_n = int(sqrt(n))

    if root_n**2 == n:
        return root_n

    print("Initializing B-Smooth Factor Base")
    factor_base = filter_base(n,B)

    while len(factor_base)<size_B:
        print("Smoothness limit is too small, incrementing by 10")
        B += 10
        factor_base = filter_base(n,B)

    smooth_nums,xlist,indices = smoothness_sieve(factor_base, n,I)

    print("Found {} smooth relations.".format(len(smooth_nums)))
    print(indices)
    print(xlist)
    print(smooth_nums)

    if len(smooth_nums) < len(factor_base):
        return("Not enough smooth numbers. Increase the sieve interval or size of the factor base.")

    print("Generating exponent vectors")
    is_square, t_matrix = gen_exponent_vectors(smooth_nums,factor_base)

    if is_square == True:
        x = smooth_nums.index(t_matrix)
        factor = gcd(xlist[x]+sqrt(t_matrix),n)
        print("Found a square!")
        return factor, n/factor
    
    print("Performing Gaussian Elimination...")
    sol_rows,marks,M = gauss_elim(t_matrix) #solves the matrix for the null space, finds perfect square
    solution_vec = solve_row(sol_rows,M,marks,0)

    print("Solving congruence of squares...")
    factor = solve(solution_vec,smooth_nums,xlist,n) #solves the congruence of squares to obtain factors

    for K in range(1,len(sol_rows)):
        if (factor == 1 or factor == n):
            print("Didn't work. Trying different solution vector...")
            solution_vec = solve_row(sol_rows,M,marks,K)
            factor = solve(solution_vec,smooth_nums,xlist,n)
        else:
            print("Found factors!")
            return factor, n/factor
    
    if (factor == 1 or factor == n):
        return("Didn't find any nontrivial factors!")

    return factor, n/factor

if __name__ == "__main__":

    n=int(input("Enter the value of n: "))
    B=int(input("Enter the value of B: "))
    I=int(input("Enter the value of I: "))
    
    print("Calculating size of factor_Base [Smoothness value (B)] according to given n...")
    size_B = calcB(n)

    '''
    #Sample Testcase
    n=15347
    B=40
    I=150
    '''
    factors = quad_sieve(n,B,size_B,I)

    if isinstance(factors,tuple):
        factor1,factor2 = factors
        print("The Factors of the number {} are {} and {}".format(n,int(factor1),int(factor2)))

    else:
        print(factors)
