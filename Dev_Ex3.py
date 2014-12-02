#Kieran Burnett
#Dev_Ex3
global cake
cake = "the cake is a lie"

def rate_chooser(from_,to_):
    if str.lower(from_[0:1]) == "p":
        if str.lower(to_[0:1]) == "e":
            rate = 1.229
        if str.lower(to_[0:1]) == "d":
            rate = 1.601
    elif str.lower(from_[0:1]) == "e":
        if str.lower(to_[0:1]) == "p":
            rate = 0.814
        if str.lower(to_[0:1]) == "d":
            rate = 1.302
    elif str.lower(from_[0:1]) == "d":
        if str.lower(to_[0:1]) == "p":
            rate = 0.625
        if str.lower(to_[0:1]) == "e":
            rate = 0.768
    return rate

def input_():
    print("Welcome to currency conversion! ")
    print("Pounds")
    print("Euros")
    print("Dollars")
    from_ = input("Please enter your starting currency: ")
    print("Pounds")
    print("Euros")
    print("Dollars")
    to_ = input("Please enter your ending value: ")
    how_much = input("Please enter how much you want to convert: ")
    return from_,to_,how_much

def convestion_calc(to_,from_,how_much):
    rate = rate_chooser(from_,to_)
    calc_val = float(how_much) * rate
    return calc_val

def output(final,to_):
    print("The final value is: ",final," ",to_)

def main():
    from_,to_,how_much = input_()
    final = convestion_calc(to_,from_,how_much)
    output(final,to_)
main()
        
