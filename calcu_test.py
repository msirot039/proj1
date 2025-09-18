print("Enter 1st Number: ")
num1 = int(input())

print("Enter 2nd Number: ")
num2 = int(input())

print("Select Operation(+,-,/,*): ")

match operation:
    case "+":
        print(f"{num1} {operation} {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} {operation} {num2} = {num1 - num2}")
    case "/":
        print(f"{num1} {operation} {num2} = {num1 / num2}")
    case "*":
        print(f"{num1} {operation} {num2} = {num1 * num2}")
