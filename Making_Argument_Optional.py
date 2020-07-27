# Making the argument optional 

def full_name (fname, mname, lname = ''):
  """This Function Makes the argument optional"""
  if lname:
    fullname = fname + ' ' + mname + ' ' + lname
  else:
    fullname = fname + ' ' + mname
  
  return fullname.title()
  
foundername = full_name('Shivam','Yadav')
print(foundername)
