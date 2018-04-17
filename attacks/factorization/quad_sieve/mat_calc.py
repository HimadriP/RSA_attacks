from itertools import chain

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
    
