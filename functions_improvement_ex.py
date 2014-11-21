# functions improvement exercise
# times-table tester
import random

# main program
def user_input():
    print("Times-table tester")
    print()
    num1 = int(input("Which times-table do you want to be tested on? "))
    return num1

def test(num1):
    for questions in range(1,6):
        num2 = random.randrange(2,13)
        ans = num1 * num2
        useranswer = int(input(str(num1) + ' x ' + str(num2) + ' = ? '))
        if useranswer == ans:
            print('Well done, you got the correct answer!')
            print()
        else:
            print('Sorry, you got the answer wrong. The correct answer is',ans)
            print()
def main():
    num1 = user_input()
    test(num1)

main()
    
              
