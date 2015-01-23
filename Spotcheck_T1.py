#Kieran burnett
#9-12-2014
#spotcheck task

def input_():
    password = input("Please enter a password 8-16 characters long: ")
    valid = validate(password)
    while valid == False:
        password = input("Please re-enter a password 8-16 characters long: ")
        valid = validate(password)

def validate(password):
    length = len(password)
    if length <= 7:
        print("Password too short")
        valid = False
    elif length >= 15:
        print("Password too long")
        valid = False
    else:
        print("Password accepted")
        valid = True
    return valid

input_()
