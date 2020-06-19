#Program to implement factorial of a number

n = eval(input("Enter a number whose factorial has to be found :")) 
fact = 1
#for factor in range(1, n+1):
 #fact = fact*factor
#Alternatively

for factor in range(n, 1, -1):
 fact = fact*factor

print("The Factorial of The number ",n, "is ",fact)
