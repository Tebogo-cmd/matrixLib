# Matrices

state = int(input("For 2x2 matrix choose 1\nFor 3x3 matrix choose 2: "))

if state == 1:
    i = 0
    matA = [int(input("Element a11: ")),int(input("Element a12: ")),int(input("Element a21: ")),int(input("Element a22: "))]
    a11 = matA[0]
    a12 = matA[1]
    a21 = matA[2]
    a22 = matA[3]
    detA = ((a11*a22) - (a12*a21))      # Determinant
    matT = [[a11,a21],[a12,a22]]        # Transpose
    matC = [[a22,-a21],[-a12,a11]]      # Cofactor
    matCT = [[a22,-a12],[-a21,a11]]     # Cofactor Transpose


    print(f"The Determinant is: {detA}")
    print(f"The matrix Transpose is: {matT}")
    print(f"The Cofactor matrix is: {matC}")

    if detA != 0:
        matIn = [[a22/detA,-a12/detA],[-a21/detA,a11/detA]]
        print(f"The Inverse is: {matIn}")
    else:
        print("Inverse Not Available since matrix provided is SINGULAR")
        
if state == 2:
    print("NOTHING")
