

# M A K I N G    A R R A Y

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
