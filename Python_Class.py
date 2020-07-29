#Class Program
class Zero(): 
  def __init__(self, name, age): #funtion parameter can be anything
    self.founder_name  = name
    self.founder_age = age 
#creating instance of class or object 
object = Zero('Shivam', 20)

print("Zero makes drone its founder is",object.founder_name)
