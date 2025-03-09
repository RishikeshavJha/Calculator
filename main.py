# Building a calculator using function, for,while loops, dictionary with the help of arithmetic and logic operators
def add(n1, n2):   #making addition function and rest are same
    return n1 + n2 #returning its value
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

operation = { #using dictionary for swiping symbols with words as we can't use special symbols for making functions.
    "+": add,
    "-": sub,
   "*": mul,
    "/": div
}

def calculator(): #for using calculator again and again with new values
    print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")
    num1 = float(input("What's the first number? :"))
    run = "y"

    while run == "y":  #using while loop for calculating with the ans

        if run == "y":
            math = input("+\n_\n*\n/\nPick an operation:")
            num2 = float(input("What's the next number? :"))
            ans = operation[math](num1, num2)
            print(f"{num1} {math} {num2} = {ans}")
            run = input(f"Type 'Y' to continue   calculating with {ans},\nor type 'New' to start a new calculation\nor 'No' for exit: ").lower()
            num1 = ans

        if run=="new":
            print("\n"*20)
            calculator()  #using Recursion:- means using function in its own function

        if run=="no":
            print("\n\nGood Bye!\nSee You Soon!")

calculator()#funtion calling