def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def modulus(x, y):
    return x % y

def calculator():
    print("Calculator Program!")
    print("----------------------------------------")
    
    while True:
        print("Select operation")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        
        try:
            # Taking input from user
            choice = input("Enter choice (1/2/3/4/5): ")

            if choice in ('1', '2', '3', '4', '5'):
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    result = add(num1, num2)
                    operator = '+'
                elif choice == '2':
                    result = subtract(num1, num2)
                    operator = '-'
                elif choice == '3':
                    result = multiply(num1, num2)
                    operator = '*'
                elif choice == '4':
                    result = divide(num1, num2)
                    operator = '/'
                elif choice == '5':
                    result = modulus(num1, num2)
                    operator = '%'

                print(f"Result: {num1} {operator} {num2} = {result}")

                # Asking user if they want to perform another calculation
                next_calculation = input("Do you want to perform another calculation? (Yes/No): ").lower()
                if next_calculation != 'yes':
                    break
            else:
                print("Invalid choice. Please enter one of 1, 2, 3, 4, 5")
        
        except ValueError as e:
            print(f"Error: {e}")
            print("Invalid input. Please enter a number.")
            continue

if __name__ == "__main__":
    calculator()
