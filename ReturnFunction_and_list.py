#function that returns a value 

def sq(x):
  
  mylist = []
  for i in range(x, 100):
    mylist.append(i)
  return mylist, x*x
  
x = int(input("Enter a number "))
List, square= sq(x)

print("List returned by function is \n",List)
print("Square of", x ,"is", square)
