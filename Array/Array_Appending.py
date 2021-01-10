

# A R R A Y     A P P E N D I N G

from array import*

arr = array('i', [ 1, 2, 3, 4, 5, 6, 7])
for i in range(len(arr)):
  print(i,"th element is ",arr[i])

# adding element to the last of the array
arr.append(5);
print("\nArray elements after appending are \n")

for i in range(len(arr)):
  print(i,"th element is ",arr[i])
