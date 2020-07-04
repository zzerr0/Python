#interactive while loop 

total = 0
count = 0
again = "yes" #it gets stored in the form of a string
#again[0] = y again[1] = e again[2] = s

while again [0] == "y" :
  #we are checking only the first letter of word yes
  number = float(input("Enter any number "))
  total = total + number
  count = count + 1
  again = input("Do you want to enter again (yes/no)")
print("The total sum of numbers is",total)
