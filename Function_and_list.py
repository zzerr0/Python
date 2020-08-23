#defining a function

def say():
  print("I am Shivam, owner of zero")
  
def primelist():
  List = []
  for i in range(1,21):
    if i % 2 is not 0:
       List.append(i)
  print(List)
  
def evenlist():
  List1 = []
  for i in range(1,21):
    if i % 2 is  0:
       List1.append(i)
  print(List1)
 
def main():
 say()
 primelist()
 evenlist()
 
main()
