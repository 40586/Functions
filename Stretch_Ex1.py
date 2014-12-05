#Kieran burnett
#Stretch_Ex1
global cake
cake = "It's a lie"

def input_():
    valid = False
    while valid == False:
        print("Please select the operation to perform(1-2):")
        print("1. Feet and Inches to Meters and Centimeters")
        print("2. Meters and Centimeters to Feet and Inches")
        con = int(input(""))
        if con == 1:
            valid = True
        elif con == 2:
            valid = True
        else:
            valid = False
    return con

def converter_sel(con):
    if con == 1:
        inch = 5000000
        while inch >= 12:
            feet = int(input("Please enter the ammount of feet: "))
            inch = int(input("Please enter the ammount of inches: "))
            if inch >= 12:
                print("invalid number of inches, must be under 12, please try again: ")
        total,total_ = im_to_me(feet,inch)
    elif con == 2:
        inch = 5000000
        while inch >= 100:
            feet = int(input("Please enter the ammount of meters: "))
            inch = int(input("Please enter the ammount of centimeters: "))
            if inch >= 100:
                print("invalid number of centimeters, must be under 100, please try again: ")
        total,total_ = me_to_im(feet,inch)
    else:
        print("You broke the program")
    return total,total_
        
def im_to_me(feet,inch):
    cm = feet * 30.48
    cm = cm + (inch * 2.54)
    meters = cm // 100
    cm = cm % 100
    return meters,cm

def me_to_im(meter,cm):
    inch = meter * 39.37
    inch = inch + (cm * 0.397)
    feet = inch // 12
    inch = inch % 12
    return feet,inch

def output(high,low,con):
    if con == 1:
        high_ = "Meters"
        low_ = "Centimeters"
    elif con == 2:
        high_ = "Feet"
        low_ = "Inches"
    print(" Your values conveted to:",high,high_,"",low,low_)

con = input_()
high,low = converter_sel(con)
output(high,low,con)
                       
