
#Implementing Class and Objects in python
class Employee :
  #constructor to initialize the valuewle 
  def __init__(self, name, age, pay) :
    #self accepts the object passed by the user
    self.name = name
    self.age = age
    self.pay = pay
  #defining a function to show the values on calling
  def show( self ) :
      return 'My name is {}, age {} amd pay {}'.format(self.name ,self.age ,self.pay)
#making an object for the class employee

obj1 = Employee("Shivam",20,200000)

#calling function with object name
print(obj1.show())

#we can also call the function with the class name
#but we've to provide object explicitly for the reference of self
#Employee.show( obj1 )
