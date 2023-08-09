# Fibonacci Sequence Function

def fibonacci_sequence(n):
    #Returns a list of the first n Fibonacci numbers.
    
    if n <= 0:
        return []

    fibonacci_numbers = [0]
    for i in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])

    return fibonacci_numbers
    