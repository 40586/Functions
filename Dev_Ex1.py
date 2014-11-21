#Kieran Burentt
#Dev_Ex1

global cake

#Convertions
def convert_hts(hours):
    t_secs = hours * 3600
    return t_secs

def convert_mts(mins):
    t_secs = mins * 60
    return t_secs

#Inputs
def user_input():
    hours = int(input("Please enter number of hours: "))
    mins = int(input("Please enter number of minutes: "))
    secs = int(input("Please enter number of seconds: "))
    return hours,mins,secs

#Calculations
def calc_t(hours,mins,secs):
    t_sec_h = convert_hts(hours)
    t_sec_m = convert_mts(mins)
    total = t_sec_h + t_sec_m + secs
    return total

#Outputs
def output(total):
    print("The total number of seconds is: ",total)

#Main
def main():
    hours,mins,secs = user_input()
    total = calc_t(hours,mins,secs)
    output(total)
    print()
    print("To run again type 'main()'")
    
main()
