def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count

user_input = input("enter the word: ")

vowel_count = count_vowels(user_input)
print("number of vowels are: ", vowel_count)