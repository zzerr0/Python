#for loop program to find the average of n-numbers
n = int(input("How many numbers do you want to enter"))
sum = 0
#Runnig for loop for n times 
for iterator in range(n):
  x = float(input("Enter Number \n"))
  sum = sum + x
print("The Average of",n,"number is",sum/n)
