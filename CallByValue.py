#reflecting the changes outside the function 
#using return method in call by value
#since changes made inside the function are not reflected outside the function using
#call by value

def getinterest(balance,rate):
  newbalance = balance * (1+rate)
  return newbalance
  
balance ,rate = eval(input("\nEmter Two Numbers with comma between them \t")) 
balance = getinterest(balance , rate)
print("The Newbalance is ",balance)
