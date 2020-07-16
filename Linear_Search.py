list = [1, 5, 10, 3, 6, 2, 14]
print("Following Items are present in List \n",list)

searchitem = int(input("Enter Number To Be Search For "))
found = False 

#Linear Search Algorithm
for i in range(len(list)):
  if list[i] == searchitem :
    found = True 
    print("Element Found At Location ", i, )
    break 
    
if found == False :
  print("Element Not Found ")
  
