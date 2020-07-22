#using multiple list 

list = [1, 2, 3, 4, 5]
main_list = [1, 3, 5]

for i in list:
  if i in main_list:
    print("Number",i, "is present in the main list")
  else :
    print("Number",i, "is not present in the main list")
