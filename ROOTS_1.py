print("""The equation is in this form: aX^2 + bX + c = d\nBut in our case d should always be zero!""")
A = float(input("Enter the coefficient of X-squared(a): "))
B = float(input("Enter the coefficient of X(b): "))
C = float(input("Enter the constant(c) in the equation: "))

x_1 = (-(((B**2)-(4*A*C))**0.5)-B)/(2*A)
x_2 = (+(((B**2)-(4*A*C))**0.5)-B)/(2*A)
print(f"The first root : x = {x_1}\nThe second root: x = {x_2}")
