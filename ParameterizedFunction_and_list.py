#defining function with arguments 
def mylist(i, l):
  li = []
  for j in range(i, l):
    li.append(j)
  print(li)
  
def say(name, age):
  print("I am", name + " my age is", age,".")
 
say("shivam"+"I am owner of zero &",21)
print("Define range of the list")
initial = int(input("Please Enter initial point"))
last = int(input("Please enter the last point")) 
mylist(initial,last)
