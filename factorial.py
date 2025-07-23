def factorial(n):
    result = 1
    for i in range (1, n+1):
        result *= i
    return result
num = int(input("enter the number: "))

if num < 0:
    print("Factorial is not defined for the negative numbers.")
else:
    print("the factorial of the", num, "is", factorial(num))