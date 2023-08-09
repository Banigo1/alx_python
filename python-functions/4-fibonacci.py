# Fibonacci Sequence Function

def fibonacci_sequence(n):
    #Returns a list of the first n Fibonacci numbers.
    
    if n == 0:
        return []

    fibonacci_numbers = [0, 1]
    for i in range(1, n):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])

    return fibonacci_numbers
    
    print(fibonacci_sequence(1))