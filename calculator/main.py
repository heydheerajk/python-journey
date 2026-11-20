
def look(a="=", b=40):
    print(a * b)


def digitcheck():
    while True:
        try:
            no = float(input("ENTER YOUR NUMBER: "))
            print("NUMBER ACCEPTED!")
            return no
        except ValueError:
            print("INVALID INPUT! ENTER A VALID NUMBER.")


def calculation():
    while True:
        look()
        print("WELCOME TO ADVANCED CALCULATOR")
        look()

        a = digitcheck()
        b = digitcheck()

        while True:
            print("\n1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Modulus")
            print("6. Power")
            print("7. Exit")

            operation = input("ENTER YOUR OPERATION: ")

            if operation == '1':
                print("RESULT:", a + b)

            elif operation == '2':
                print("RESULT:", a - b)

            elif operation == '3':
                print("RESULT:", a * b)

            elif operation == '4':
                if b == 0:
                    print("CANNOT DIVIDE BY ZERO!")
                else:
                    print("RESULT:", a / b)

            elif operation == '5':
                if b == 0:
                    print("CANNOT USE MODULUS WITH ZERO!")
                else:
                    print("RESULT:", a % b)

            elif operation == '6':
                print("RESULT:", a ** b)

            elif operation == '7':
                print("THANK YOU FOR USING CALCULATOR!")
                return

            else:
                print("INVALID OPERATION! TRY AGAIN.")


calculation()
