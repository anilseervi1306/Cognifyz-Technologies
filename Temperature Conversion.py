def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter the choice (1 or 2): ")
    
#Conversion of Celsius to Fahrenheit
    if choice == '1':
        celsius = float(input("Enter temperature in celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
    
#Conversion of Fahrenheit to Celsius
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")
        
    else:
        print("Invalid choice. Please enter either 1 or 2 ")
    
if __name__ == "__main__":
    main()