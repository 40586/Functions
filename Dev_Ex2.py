def input_odd():
    check = 0
    while check != 1:
        num = int(input("Please enter a odd number: "))
        check = num % 2
    return num
def calc_out_1(start,end,step,num):
    for count in range(start,end,step):
        print("{0:^{1}}".format(count * "*",num))
def main():
    num = input_odd()
    calc_out_1(1,num,2,num), calc_out_1(num,0,-2,num)
    
