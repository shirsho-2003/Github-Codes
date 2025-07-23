numbers = input("enter numbers seperated by spaces: ")

numbers_list = [float(num) for num in numbers.split()]

largest = max(numbers_list)

print("the largest number is: ", largest)