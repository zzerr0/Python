#Maximum of three numbers 
x1, x2, x3 = eval(input("Input 3 numbers "))
if x1>=x2 and x1>=x3:
  maxval = x1
elif x2>=x1 and x2>=x3:
  maxval = x2
else:
  maxval = x3
print("The maximum number is ",maxval)
