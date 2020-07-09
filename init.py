#class program to implement __init__

class Admi:
  def __init__(constructor,name, age):
  #here self is reference to the current Instance of class  
    constructor.name = name 
    constructor.age = age 
  def main(self):
   print("My name is",self.name)

object = Admi("Shivam",34)
object.main()
