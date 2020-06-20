def fun():
  fst = input("Enter Your First Name : ")
  sec = input("Enter Your Second Name : ")
  uname = fst[0]+sec[:5]
  print(uname)
  print(fst[0],".",sec)
  
fun()
