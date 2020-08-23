#this program is to show append() method

#initialzing a list with no items
list = []
for i in range(1,11):
  list.append(i)
  
print(list[:])
print("Sum of first 10 number is ",sum(list))
print("Sum of first 4 number is ",sum(list[:4]))
