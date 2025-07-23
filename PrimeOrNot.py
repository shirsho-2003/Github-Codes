def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) +1):
        if num % i == 0:
            return False
    return True

n = int(input("enter a number: "))

if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number." )