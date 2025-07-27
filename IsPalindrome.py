def is_palindrome(string):
    string = string.replace(" ", "").lower()
    
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False
string = input("enter the string: ")

if is_palindrome(string):
    print("The string is palindrome.")
else:
    print("This is not palindrome.")