

#  S E A R C H I N G   I N    A R R A Y

from array import*

arr = array('i')
print("How many enters you want to enter ")
n = int(input())
print("Enter the",n, "values for array")
for i in range(n):
  arr.append(int(input()))
print("Values Entered ")
print("The array elements are")
for i in range(len(arr)):
  print(arr[i])
  
print("Enter the element to be searched ")
value = int(input())
# LINEAR SEARCHING IN ARRAY
for i in range(len(arr)):
  if arr[i] == value:
    print("Value found at location", i)
