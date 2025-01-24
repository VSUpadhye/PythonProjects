def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
continue_with_answer = "y"
status = "y"
first_num = float(input("Enter the first number: "))
while status:
    operator = input("Enter the operation to be performed (+, -, *, /): ")
    second_num = float(input("Enter the second number: "))
    answer = operations[operator](n1 = first_num, n2 = second_num)
    print(f"{first_num} {operator} {second_num} = {answer}")
    status = input("To continue type 'yes' otherwise type 'end' to stop: ")
    if status == "end":
            exit()
    continue_with_answer = input(f"Type 'y' to continue with the {answer}. Type 'n' to start new calculation: ")
    if continue_with_answer == "n":
        print("\n" * 10)
        first_num = float(input("Enter the first number: "))
    else:
        first_num = answer