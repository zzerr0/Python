#function Returning more than 1 Value

def prodiv(numberA,numberB):
  pro = numberA * numberB
  div = numberA/numberB
  return pro, div
  
numA, numB = eval(input("\nEmter Two Numbers with comma between them \t")) 
product, division = prodiv(numA, numB)
print("The product of",numA, numB ,"is",product)
print("The division of",numA, numB ,"is",division)
