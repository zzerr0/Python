def decide(list): 
  fn = list[0]
  ln = list[-1]  # -1 indicates the last element -2 = second last and so on
  if fn == ln:
    return True
  else:
    return False
    
    
list = [1, 3, 4, 5, 81]
print("The result is", decide(list))
