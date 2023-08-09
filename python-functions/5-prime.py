# Prime Number Function

def is_prime(number):
    if number <= 1:
        # 1 is not a prime number, return False
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            # Divisor found, number is not prime; return False
            return False
    
    # No divisor found, number is prime; return True
    return True

"""
def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False   
    return True         

"""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
