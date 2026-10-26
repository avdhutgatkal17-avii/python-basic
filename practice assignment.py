# count a vowels from a string without using a for loop


input_string = input("Enter a string: ")
vowel_count = input_string.lower().count('a') + input_string.lower().count('e') + input_string.lower().count('i') + input_string.lower().count('o') + input_string.lower().count('u')
print("Number of vowels in the string: ", vowel_count)
