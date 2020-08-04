
def reverse(String):
  return String[::-1]

mystring = input("Enter the number")
if mystring == reverse(mystring):
  print(mystring, "is equal")
else:
  print("Not Equal")
