# Fibonacci Sequence Function
def fibo(n):
    if n == 1:
        return 1
        
    elif n == 0:
        return 0
    
    elif n > 1:
        return fibo(n-1) + fibo(n-2)
        
       
    #Returns a list of the first n Fibonacci numbers.
    def fibonacci_sequence(t):
        lis = []
    for i in range():
        lis.append(fibo(i))
        return lis
    
    def main():
        num = int(input())
        print(fibonacci_sequence(num))
        pass
    
    if __name__ == "__main__":
        main()