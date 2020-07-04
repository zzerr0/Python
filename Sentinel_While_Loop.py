#sentinel while loop to find the average of numbers
#sentinel loop keeps executing until a special value is arrived
#which tell the end signal
#that special value is called sentinel value
#in the below program a negative number is a sentinel value
total = 0 
count = 0
number = float(input("Enter the Number"))
while(number >= 0):
  total = total + number
  count = count + 1
  number = float(input("Enter the Number (-ve to exit the loop)"))
print("The average of numbers is",total/count)
