#Function Returning A Value

def full_name( fname, lname):
  """this function returns the full name"""
  fullname = fname + ' ' + lname
  return fullname.title()
  
ownername = full_name('$H|√AM', 'YADAV')
print("Company's owner name is " ,ownername )
