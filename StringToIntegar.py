def string_to_integar(string_number):
    try:
        return int(string_number)
    except ValueError:
        return "Invalid Input, Try To Input Numeric Integars."

input = input("enter a number as a string: ")
converted_result = string_to_integar(input)
print("The converted result is: ", converted_result)