

# A R R A Y      D E L E T I N G

from array import*

arr = array('i', [ 1, 2, 3, 4, 5, 6, 7])
for i in range(len(arr)):
  print(i,"th element is ",arr[i])

# deleting element from the array
# we can delete an element from array in two ways
# By value -> using remove & By index -> using pop

# By VALUE
print("Enter the Value to be deleted from array")
value = int(input())
arr.remove(value)
print("Array after deleting by Value is ")
for i in range(len(arr)):
  print(i,"th element is ",arr[i])
  
#By INDEX
print("Enter index whose value has to be deleted from array")
index = int(input())
arr.pop(index)
print("Array after deleting by Index is ")
for i in range(len(arr)):
  print(i,"th element is ",arr[i])
