#Program to find solution for quadratic equation
#A Quadratic equation is AX^2+BX+C=0
#Where value of x is given by (-B + √B^2-4A^2) / 2a
import cmath
a = eval(input("\n Enter the value of a  :"))
b = eval(input("\n Enter the value of b  :"))
c = eval(input("\n Enter the value of c  :"))
sq = cmath.sqrt(b*b-4*a*a)
root1 = (-b+sq)/2*a
root2 = (-b-sq)/2*a

print("The Two Solutions For Quadratic Equations are \n")
print(root1, root2)
