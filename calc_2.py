def main():
    operation = input("Press 1 for addition, 2 for subtraction, 3 for multiplication, 4 for divition, 5 for exponents, 6 for square roots and 7 to exit ")
    if operation=="1":
        num1 = input("Enter first number. ")
        num2 = input("Enter your second number. ")
        num1 = int(num1)
        num2 = int(num2)
        print(num1+num2)
        restart=input("Press one to restart ")
        if restart=="1":
            main()
        else:
            exit()
    if operation=="2":
        num1 = input("Enter first number. ")
        num2 = input("Enter your second number. ")
        num1 = int(num1)
        num2 = int(num2)
        print(num1-num2)
        restart=input("Press one to restart ")
        if restart=="1":
            main()
        else:
            exit()
    if operation=="3":
        num1 = input("Enter first number. ")
        num2 = input("Enter your second number. ")
        num1 = int(num1)
        num2 = int(num2)
        print(num1*num2)
        restart=input("Press one to restart ")
        if restart=="1":
            main()
        else:
            exit()
    if operation=="4":
        num1 = input("Enter first number. ")
        num2 = input("Enter your second number. ")
        num1 = int(num1)
        num2 = int(num2)
        print(num1/num2)
        restart=input("Press one to restart ")
        if restart=="1":
            main()
        else:
            exit()
    if operation=="5":
        num1=input("Enter number here ")
        num2=input("Enter exponent here ")
        num1=int(num1)
        num2=int(num2)
        print(num1**num2)
        restart=input("Press one to restart ")
        if restart=="1":
            main()
        elif restart=="7":
            x=0
            while x<5000:
                print("Eight minutes to the destruction of Earth")
                x = x+1
        else:
            exit()
    if operation=="6":
        num1=input ("What number would you like to know the square root of ")
        num1=int(num1)
        print (num1**0.5)
        restart=input("Press one to restart ")
        if restart=="1":
            main()
        else:
            exit()
    if operation>="7":
        exit()
main()