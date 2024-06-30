def fibonacci_series(n):
    series = []
    a, b = 0, 1

    while len(series) < n:
        series.append(a)
        a, b = b, a + b

    return series

# Test the program
number = int(input("Enter the number of terms: "))
Fibonacci_series = fibonacci_series(number)

print("Fibonacci Series:")
print(Fibonacci_series)