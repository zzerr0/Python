classmate = {'shivam':'college','shubham':'Job'}
friends = ['Raju', 'shivam', 'shubham']

for name in classmate.keys():
  print(name)
  #if name is present in friends list
  if name in friends:
    print("Hello",name, "You are common ")
    print("You do",classmate[name])
  else:
    print("Nothing Common")
