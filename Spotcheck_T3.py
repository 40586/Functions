#Kieran burnett
#spotcheck Task 3

def get_input():
    distance = int(input("Please enter the distance of the journey: "))
    miles_per = int(input("Please enter the miles per gallon of the vehicle: "))
    fuel_price = float(input("Please enter the current price of fuel: "))
    return distance,miles_per,fuel_price

def calculate_cost(distance,miles_per,fuel_price):
    miles_per = miles_per * 4.55
    liters_used = distance / miles_per
    price = liters_used * fuel_price
    return price

def display_cost(price):
    print("The cost of fuel for the journey should be displayed as £8.32 ")

# main program
d,m,f = get_input()
price = calculate_cost(d,m,f)
display_cost(price)
