




class Node:
  def __init__(self, data = None, nxt = None ):
    self.data = data
    self.nxt = nxt
    
class linkedlist:
  def __init__(self) :
    self.head = None
    
  #Defining a Function for insertion
  
  def insert(self, data):
    newnode = Node( data, self.head )
    self.head = newnode
  
  #Defining a function for printing
  def print(self):
    #initializing an iterator
    itr = self.head
    while itr:
      print(itr.data)
      itr = itr.nxt
      
      
#the main function

if __name__ == "__main__":
  #creating an object of linkedlist class
  obj = linkedlist()
  print("The linked list is ")
  obj.insert(5)
  obj.insert(9)
  obj.print()
    
