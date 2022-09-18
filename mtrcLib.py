  # name : dt
  # date: Sunday 11 Sep 2022
  # type: Library/Api
  # name of progm: mtrcLib.py
  # discription: 
  # This is a Library for matrices
 # I will primarily be workind with 2X2 and 3x3 square matrices:
 # To keep things simple regarding user input, only two  inputd will be required.
 # This will be the matrix choice and the matrix


state = int(input("For 2x2 matrix choose 1\nFor 3x3 matrix choose 2: "))
def detF(w,x,y,z):                              #Function for computing det
        return ((w*z) - (x*y))

if state == 1:
    matA = [[float(input("Element a11: ")),float(input("Element a12: "))],[float(input("Element a21: ")),float(input("Element a22: "))]]
    a11 = matA[0][0]
    a12 = matA[0][1]
    a21 = matA[1][0]
    a22 = matA[1][1]
    detA = detF(a11,a12,a21,a22)        # Determinant
    matT = [[a11,a21],[a12,a22]]        # Transpose
    matC = [[a22,-a21],[-a12,a11]]      # Cofactor
    matCT = [[a22,-a12],[-a21,a11]]     # Cofactor Transpose
    matI =  [[1,0],[0,1]]               # identity matrix

    print(f"Matrix given: {matA}")
    print(f"Determinant: {detA}")
    print(f"Matrix Transpose: {matT}")
    print(f"Cofactor matrix: {matC}")
    print(f"Identity matrix: {matI}")

    if detA != 0:
        matIn = [[a22/detA,-a12/detA],[-a21/detA,a11/detA]]
        print(f"Inverse: {matIn}")
    else:
        print("Inverse Not Available since matrix provided is SINGULAR")
        
if state == 2:
    matB = [float(input("Element a11: ")),float(input("Element a12: ")),float(input("Element a13: "))]
    a11 = matB[0] ; a12 = matB[1] ; a13 = matB[2]
    matB = matB+[float(input("Element a21: ")),float(input("Element a22: ")),float(input("Element a23: "))]
    a21 = matB[3] ; a22 = matB[4] ; a23 = matB[5]
    matB = matB+[float(input("Element a31: ")),float(input("Element a32: ")),float(input("Element a33: "))]
    a31 = matB[6] ; a32 = matB[7] ; a33 = matB[8]
    # Done with user input for 3x3 now building the 2Dmatrix

    matB = [[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]]

    Id_matB = [[1,0,0],[0,1,0],[0,0,1]]

    print(f"Matrix given is: {matB}")
    print(f"Identity matrix: {Id_matB}")
    # Taking The determinant along the first the row
    detB  =  (a11*detF(a22,a23,a32,a33))
    detB += (-a12*detF(a21,a23,a31,a33))
    detB += (a13*detF(a21,a22,a31,a32))
    print(f"Determinant is: {detB}")
    #   building the adjoint of B -> for inverse calculation
    Co_matB = [[detF(a22,a23,a32,a33),(-1)*detF(a21,a23,a31,a33),detF(a21,a22,a31,a32)],[(-1)*detF(a12,a13,a32,a33),detF(a11,a13,a31,a33),(-1)*detF(a11,a12,a31,a32)],[detF(a12,a13,a22,a23),(-1)*detF(a11,a13,a21,a23),detF(a11,a12,a21,a22)]]
    print(f"Co-factor matrix: {Co_matB}")
    Adj_matB = [[Co_matB[0][0],Co_matB[1][0],Co_matB[2][0]],[Co_matB[0][1],Co_matB[1][1],Co_matB[2][1]],[Co_matB[0][2],Co_matB[1][2],Co_matB[2][2]]]
    print(f"Adjoint matrix:  {Adj_matB}")
    if detB == float(0):
    	print("Inverse not possible since matrix is SINGULAR")
    else:
        row = 0
        col  = 0
        Inv_matB = [[0,0,0],[0,0,0],[0,0,0]]
        while True:
           Inv_matB[row][col] = (1/detB)*			                 Adj_matB[row][col]
           row+=1
           col+=1
           if (row== 3) and (col == 3):
           	break
           else:
           	continue
        print(f"Matrix Inverse: {Inv_matB}")
    	  	
    	  
    	  
    	  
    	  
