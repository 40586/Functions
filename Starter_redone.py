#Kieran Burnett
#Calulate pay

def calc_basic_pay(hours,pay):
    total = hours * pay
    return total

def calc_overtime_pay(hours,pay):
    o_hours = hours - 40
    o_pay = pay * 1.5
    sub_total = o_pay * o_hours
    sub_total_2= pay * 40
    total = sub_total + sub_total_2
    return total

def calc_total_pay(hours,pay):
    if hours <= 40:
        total = calc_basic_pay(hours,pay)
    else:
        total = calc_overtime_pay(hours,pay)
    return total

def work_details():
    hours = int(input("Please enter hours worked: "))
    pay = int(input("Please enter pay per hour: "))
    return hours,pay
#hours,pay = work_details()

def display_total_pay(total):
    print(" Your total pay is: £",total)

def calculate_pay():
    hours,pay = work_details()
    total = calc_total_pay(hours,pay)
    display_total_pay(total)

calculate_pay()
