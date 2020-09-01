#implementing Binary Tree 
#first of all we have to create a node that can hold
#value and position of left and right child
# 2 and 3 become left and right children of 1 

     #      1 
     #    /   \ 
     #  Left  Right
 
class Node:
   def __init__(self, key):
     self.left = None
     self.right = None
     self.value = key
     
     
#now we have successfully created a node 
#now we have to create a tree so that we can bind these 
#nodes together
#therefore we'll create a roor node


root = Node(1)
root.left = Node(10);
root.left = Node(30);   
root.right = Node(20);         

