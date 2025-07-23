def sum_of_digit(number):
    total = 0
    while number>0:
        digit = number % 10
        total += digit
        number //= 10
    return total
num = int(input("Enter a number: "))
result = sum_of_digit(abs(num))
print("sum of digit: ", result)