import art

def add(n1, n2):
    return n1 + n2

def subtract (n1,n2):
    return n1-n2

def multiplication (n1, n2):
    return  n1 * n2

def divide (n1, n2):
    return n1/n2

print(art.logo)

while True:
    operation = input("please select the operation that you would like to do, add, subtract, multiplication, or division.")
    n1 = int(input("please input the first number."))
    n2 = int(input("please input the second number."))
    operation_total = 0
    if operation.lower() == "add":
        operation_total = add(n1, n2)
        print(f"Answer:{operation_total}")
    elif operation.lower() == "subtract":
        operation_total = subtract(n1, n2)
        print(f"Answer:{operation_total}")
    elif operation.lower() == "multiply" or "multiplication":
        operation_total = multiplication(n1, n2)
        print(f"Answer:{operation_total}")
    elif operation.lower() == "division":
        operation_total = divide(n1, n2)
        print(f"Answer:{operation_total}")

    go_again = input("would you like to do another operation? 'yes' or 'no'.")
    if go_again.lower() == "no":
        break
