# import module
from tabulate import tabulate

#Creating Neville's Method
print("QUESTION 1")
print("Neville's Method")
# Value we're estimating for
mainx = 3.7
# X-values
x0 = 3.6
x1 = 3.8
x2 = 3.9
# F(x) values
fx0 = 1.675
fx1 = 1.436
fx2 = 1.318

# Finding i=1 First Degree
q11 = (1/((x1)-(x0)))*((((mainx)-(x0))*(fx1))-(((mainx)-(x1))*(fx0)))
print("The Q 1,1 value: ", q11)

# Finding i=2 First Degree
q21 = (1/((x2)-(x1)))*((((mainx)-(x1))*(fx2))-(((mainx)-(x2))*(fx1)))
print("The Q 2,1 value: ", q21)

# Finding i=2 Second Degree
q22 = (1/((x2)-(x0)))*((((mainx)-(x0))*(q21))-(((mainx)-(x2))*(q11)))
print("The Q 2,2 value: ", q22)

# Using Newton's Forward Method for Questions 2 and 3
print("\nQUESTION 2")
print("Newton's Forward Method")
# X-values
x1 = 7.2
x2 = 7.4
x3 = 7.5
x4 = 7.6
# F(x) values
fx1 = 23.5492
fx2 = 25.3913
fx3 = 26.8224
fx4 = 27.4589
# Finding first directional derivative first degree
firstddi1 = ((fx2)-(fx1))/((x2)-(x1))
print("First Direction Derivate 1st degree is: ", firstddi1)
# Finding first directional derivative second degree
firstddi2 = ((fx3)-(fx2))/((x3)-(x2))
print("First Direction Derivate 2nd degree is: ", firstddi2)
# Finding first directional derivative third degree
firstddi3 = ((fx4)-(fx3))/((x4)-(x3))
print("First Direction Derivate 3rd degree is: ", firstddi3)

# Finding second directional derivative second degree
secondddi2 = ( ( ((fx3)-(fx2))/((x3)-(x2)) ) - ( ((fx2)-(fx1))/((x2)-(x1)) )  ) / ((x3)-(x1))
print("Second Direction Derivate 2nd degree is: ", secondddi2)

# Finding second directional derivative third degree
secondddi3 = ( ( ((fx4)-(fx3))/((x4)-(x3)) ) - ( ((fx3)-(fx2))/((x3)-(x2)) )  ) / ((x4)-(x2))
print("Second Direction Derivate 3nd degree is: ", secondddi3)

# Finding third directional derivative third degree
thirdddi3 = (((((fx4 - fx3) / (x4 - x3)) - ((fx3 - fx2) / (x3 - x2))) / (x4 - x2)) - ((((fx3 - fx2) / (x3 - x2)) - ((fx2 - fx1) / (x2 - x1))) / (x3 - x1))) / (x4 - x1)
print("Third Direction Derivate 3rd degree is: ", thirdddi3)

# Continuing Newton's Forward Method for Question 3
print("\nQUESTION 3")
print("Newton's Forward Method")
# Finding the first degree approximation
p1 = (fx1) + ((firstddi1)*((7.3)-(x1)))
print("First Degree Approximation", p1)

# Finding the second degree approximation
p2 = (p1) + ((secondddi2)*((7.3)-(x1))*((7.3)-(x2)))
print("Second Degree Approximation", p2)

# Finding the third degree approximation
p3 = (p2) + ((thirdddi3)*((7.3)-(x1))*((7.3)-(x2))*((7.3)-(x3)))
print("Third Degree Approximation", p3)

# Using Hermite Divided Difference Method for Question 4
print("\nQUESTION 4")
print("Hermite Divided Difference Method")

# Main Z-values
z0 = 3.6
z1 = 3.6
z2 = 3.8
z3 = 3.8
z4 = 3.9
z5 = 3.9
# Main f(x) values
f0 = 1.675
f1 = 1.675
f2 = 1.436
f3 = 1.436
f4 = 1.318
f5 = 1.318
# Finding first directional derivative z1
z1firstdd = -1.195
print("z1 First Directional Derivative is: ", z1firstdd)
# Finding first directional derivative z2
z2firstdd = ((f3)-(f1))/((z3)-(z1))
print("z2 First Directional Derivative is: ", z2firstdd)
# Finding first directional derivative z3
z3firstdd = -1.188
print("z3 First Directional Derivative is: ", z3firstdd)
# Finding first directional derivative z4
z4firstdd = ((f5)-(f3))/((z5)-(z3))
print("z4 First Directional Derivative is: ", z4firstdd)
# Finding first directional derivative z5
z5firstdd = -1.182
print("z5 First Directional Derivative is: ", z5firstdd)

print("\n")

# Finding second directional derivative z2
z2seconddd = ((z2firstdd)-(z1firstdd))/((z2)-(z0))
print("z2 Second Directional Derivative is: ", z2seconddd)
# Finding second directional derivative z3
z3seconddd = ((z3firstdd)-(z2firstdd))/((z3)-(z1))
print("z3 Second Directional Derivative is: ", z3seconddd)
# Finding second directional derivative z4
z4seconddd = ((z4firstdd)-(z3firstdd))/((z4)-(z2))
print("z4 Second Directional Derivative is: ", z4seconddd)
# Finding second directional derivative z5
z5seconddd = ((z5firstdd)-(z4firstdd))/((z5)-(z3))
print("z5 Second Directional Derivative is: ", z5seconddd)

print("\n")

# Finding third directional derivative z3
z3thirddd = ((z3seconddd)-(z2seconddd))/((z3)-(z0))
print("z3 Third Directional Derivative is: ", z3thirddd)
# Finding third directional derivative z4
z4thirddd = ((z4seconddd)-(z3seconddd))/((z4)-(z1))
print("z4 Third Directional Derivative is: ", z4thirddd)
# Finding third directional derivative z5
z5thirddd = ((z5seconddd)-(z4seconddd))/((z5)-(z2))
print("z5 Third Directional Derivative is: ", z5thirddd)

print("\n")

# Finding fourth directional derivative z4
z4fourthdd = ((z4thirddd)-(z3thirddd))/((z4)-(z0))
print("z4 Fourth Directional Derivative is: ", z4fourthdd)
# Finding fourth directional derivative z5
z5fourthdd = ((z5thirddd)-(z4thirddd))/((z5)-(z1))
print("z5 Fourth Directional Derivative is: ", z5fourthdd)

print("\n")

# Finding fifth directional derivative z5
z5fifthdd = ((z5fourthdd)-(z4fourthdd))/((z5)-(z0))
print("z5 Fifth Directional Derivative is: ", z5fifthdd)

print("Final Matrix")
# Assigning Data
Matrix4 = [
      [z0, f0, 0, 0, 0, 0, 0],
      [z1, f1, z1firstdd, 0, 0, 0, 0],
      [z2, f2, z2firstdd, z2seconddd, 0, 0, 0],
      [z3, f3, z3firstdd, z3seconddd, z3thirddd, 0, 0],
      [z4, f4, z4firstdd, z4seconddd, z4thirddd, z4fourthdd, 0],
      [z5, f5, z5firstdd, z5seconddd, z5thirddd, z5fourthdd, z5fifthdd]
]

# Displating 4x4 matrix
print(tabulate(Matrix4))

# Question 5
print("\nQUESTION 5")
# Main X-values
x0 = 2
x1 = 5
x2 = 8
x3 = 10
# Main Y-Values
a0 = 3
a1 = 5
a2 = 7
a3 = 9
# Finding h0, h1, h2
h0 = ((x1)-(x0))
print(h0)
h1 = ((x2)-(x1))
print(h1)
h2 = ((x3)-(x2))
print(h2)

# Solving for points in the matrix
r2c2 = (2*((h0)+(h1)))
r3c3 = (2*((h1)+(h2)))

print("Matrix A")
# Assigning Data
MatrixA = [
      [1, 0, 0, 0],
      [h0, r2c2, h1, 0],
      [0, h1, r3c3, h2],
      [0, 0, 0, 1]
]

# Displating 4x4 matrix
print(tabulate(MatrixA))

print("Vector b")

b2 = (( ((3)/(h1)) * ((a2)-(a1)) ) - ( ((3)/(h0)) * ((a1)-(a0)) )    )
b3 = (( ((3)/(h2)) * ((a3)-(a2)) ) - ( ((3)/(h1)) * ((a2)-(a1)) )    )

# Assigning Data
VectorB = [
      [0],
      [b2],
      [b3],
      [0]
]

# Displating Vector B
print(tabulate(VectorB))

print("Vector x")

c0 = 0
c3 = 0
c1 = -1/37
c2 = 4/37

# Assigning Data 
Vectorx = [
      [c0],
      [c1],
      [c2],
      [c3]
]

# Displating Vector C
print(tabulate(Vectorx))


