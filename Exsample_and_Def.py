#Kieran Burnett
#Uses of these things


cake = " is a lie"

def exsample(parameter): #A parameter is a required vaule that the user has to put into the function for it to work
    global cake # a global varable is a variable that can be accessed by anything in the program
#it is also the DEVIL HIMSELF
    parameter = parameter + cake # parameter is a local varible, this means it is only used by the function it is within, and cannot be edited by other parts of the program
    return parameter # a return value, mean the function assignes the value to the varible "sentance = exsample("The cake")"

def main():
    sentance = exsample("The cake") # "The cake" is an argument, this will be bound to the parameter of the function you are using
    print(sentance)
main()
