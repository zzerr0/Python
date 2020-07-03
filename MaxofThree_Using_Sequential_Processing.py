#Maximum of three numbers using Sequential Processing
x1, x2, x3, x4 = eval(input("Input 4 numbers"))
#Devision Tree
maxval = x1 
if x2 >= maxval:
  maxval = x2
if x3 >= maxval:
  maxval = x3
if x4 >= maxval:
  maxval = x4
  
print("The Maximum elemes out of these there",x1, x2, x3, x4)
print("is",maxval); 
