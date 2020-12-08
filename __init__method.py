

# __init__ method
# the init method acts as an constructor
# for example 

class Person:
  # inite method to Initiliaze the name 
 def __init__(self, name, age, a, b):
   
   #self.name acts as a variable 
    self.name  = name
    self.age = age
    self.c = a+b
    self.a = a
  #defining a method which will use name data member
 def sayname(self):
   print("My name is ", self.name )
   print(" and my age is ", self.age )
   print(self.c) 

p = Person('Shivam Yadav', 44,4,5)
p2 = Person('Shubham Yadav', 21,6,7)
p.sayname();
p2.sayname();
