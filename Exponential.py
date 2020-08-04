print("Yes")

def calc(base, exp):
  pro = 1
  num = exp
  while num > 0:
   pro = pro * base
   num = num - 1
  return pro

base = 2
exp = 3
pro = calc(base, exp)
print(pro)
