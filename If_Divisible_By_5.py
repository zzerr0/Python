#print only those numbers which are divisible by 5
def division(list):
  for i in list:
    if (i % 5 == 0):
      print(i)


list = [1, 5, 10, 11, 12, 15, 19, 20, 25]
division(list)
