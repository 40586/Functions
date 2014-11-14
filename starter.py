#Kieran burnett
#Starter program

b_hours = int(input("Please enter the number of basic hours worked: "))
e_hours = int(input("Please enter the number of overtime hours worked: "))
pay = int(input("Please enter your pay per hour: "))

o_pay = pay + (pay / 2)
overtime = e_hours * o_pay
basic = b_hours * pay

total = basic + overtime
print("Your total pay is: £",total)
