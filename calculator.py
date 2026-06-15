while True:
    print("1-Add    2-Subtract    3-Division   4-Power  5-Multiplication  0-Stop")    
    choice = input("Enter: ").strip()

    if choice == "+" or choice == "1" or choice.lower() == "add":
        num = eval(input("Enter the first number: "))
        num2 = eval(input("Enter the second number: "))
        print(num+num2)

    elif choice == "-" or choice == "2" or choice.lower() == "subtract":
        num = eval(input("Enter the first number: "))
        num2 = eval(input("Enter the second number: "))
        print(num-num2)

    elif choice == "/" or choice == "3" or choice.lower() == "division":
        num = eval(input("Enter the first number: "))
        num2 = eval(input("Enter the second number: "))
        while num2 == 0:
            num2 = eval(input("You cannot divide by zero: "))
        print(num/num2)
        
    elif choice == "**" or choice == "4" or choice.lower() == "power":
        num = eval(input("Enter the first number: "))
        num2 = eval(input("Enter the second number: "))
        print(num**num2)

    elif choice == "*" or choice == "5" or choice.lower() == "multiplication":
        num = eval(input("Enter the first number: "))
        num2 = eval(input("Enter the second number: "))
        print(num*num2)
    
    elif choice == "0" or choice == "stop":
        print("Calculator has stopped")
        break
