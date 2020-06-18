#Program to implement Calculate interest amount

p = eval(input("Enter the Principal amount "))
apr = eval(input("Enter the interest rate "))
x = eval(input("Enter the Time duration "))
for i in range(x):
 p = p * (1+apr)
 
print(p,"Is the interest rate after 10 years")
