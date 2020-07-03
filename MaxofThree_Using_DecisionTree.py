#Maximum of three numbers using decision tree
x1, x2, x3 = eval(input("Input 3 numbers"))
#Devision Tree
if x1>=x2:
  if x1>=x3:
    maxval = x1
  else:
    maxval = x3
if x2>=x1:
  if x2>=x3:
    maxval = x2
  else:
    maxval = x3
print("The Maximum elemes out of these there",x1, x2, x3)
print("is",maxval); 
