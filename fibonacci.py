def fibonacci_series(n):
    a, b = 0 ,1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b

num = int(input("Enter the length of the numbers: "))
fibonacci_series(num)