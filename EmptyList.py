list = []
#this is an empty lits 
#we are going to fill this list with positive integers

x = float(input("Enter a positive integer "))
while x >= 0:
  list.append(x)
  x = float(input("Enter a positive integer "))
  
print(list)
