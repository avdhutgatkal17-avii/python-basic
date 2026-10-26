# 3. accept the name and check if its palindrome.
name = input(" Enter a name : ")
if name == name[::-1]:
    print(" The name is a palindrome.")
else:
    print(" the name is not a palindrome.")
