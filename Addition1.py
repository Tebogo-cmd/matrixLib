# Add two matrices


def build_mat():
    k = 0
    matK = []
    std_var = "k"
    n = 1 # row one
    while True:
        std_var = [input(f"Row Element {n}: ")]
        
       
        if std_var == ['E'] or std_var == ['e']:     # std_var --> used to stop the input of matrix elememts
            break
        if std_var == ['N'] or std_var == ['n']:     # std_var --> used to define a new matrix
            n += 1
        else:
            matK = matK + std_var
            matK[k] = float(matK[k])
            k += 1
            continue
    matK = matK + [n]
    return matK

print("Please Enter matrix A ")
matA = build_mat()
len_matA = len(matA) - 1  # n -> lst element
print("Please Enter matrix B ")
matB = build_mat()
len_matB = len(matB) -1 
if len_matA != len_matB: 
    print(f"Matrix A is: {matA}\nMatrix B is: {matB}")
    print("Addition not Possile: Matrices need to be of the same order")
else:   #perform addition 
    print(f"Matrix A is: {matA}\nMatrix B is: {matB}")
    a_plus_b = []  # seen as one list
    counter = 0
    while True:
        
        if counter == len_matA:
            break
        else:
            temp = matA[counter] + matB[counter]
            temp = [temp]
            a_plus_b = a_plus_b + temp
            counter += 1
            continue
    
    A_plus_B = []    # seen as Rows and cols
    n = matA[-1]
    group = (len_matA/n)
    count = 0
    stopper = 0
    dump = []
    # Below is the code for formatting a_plus_b -> A_plus_B
    while True:
        dump = dump + [a_plus_b[count]]
        count+=1
        if (count % group) == 0:
            A_plus_B = A_plus_B + [dump]
            dump = []
            stopper += 1
            
        if stopper == n:
            break  #Done formatting a_plus_b 
        else:
            continue
    #print(f"The primary 1D mat: {a_plus_b}")  
    print(f"Matrix A + Matrix B = {A_plus_B}")
        
