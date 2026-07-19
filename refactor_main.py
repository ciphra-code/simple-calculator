def input_two_number ():
    a = float(input("a: "))
    b = float(input("b: "))
    return a, b
def input_one_number ():
    a = float(input("a: "))
def plus (a, b):
    return a + b
def sub (a, b):
    return a - b
def mul (a, b):
    return a * b
def division (a, b):
    if b == 0:
        return "Cannot divide by zero"
    
    return a / b
def square ( a):
    return a ** 2
def even_or_odd (a):
    return a % 2 == 0
def absolute (a):
    return abs(a)
while True:
    print("=========Calculator=========")
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Squaring")
    print("6. Check even or odd")
    print("7. Absolute value")
    print("0. Back")
    print()
    print("=============================")
    
    choice = int(input("Feature:"))

    if choice == 1:
        a, b = input_two_number()

        print (plus(a,b))
    
    elif choice == 2:
        a, b = input_two_number()

        print(sub(a,b))

    elif choice == 3:
        a, b = input_two_number()

        print(mul(a, b))

    elif choice == 4:
        a, b = input_two_number()

        print(division(a, b))

    elif choice == 5:
        a = input_one_number ()

        print(square(a))

    elif choice == 6:
        a = int(input("a: "))

        if even_or_odd (a):
            print("Even")
        else:
            print("Odd")

    elif choice == 7:
        a = input_one_number ()

        print(absolute(a))

    elif choice == 0:
        print("Thank you!")
        break
    else:
        print("Invalid choice")
