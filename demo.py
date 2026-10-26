
text = " welcome to imcc "
print(" welcome to imcc : ", text.capitalize())
text = text.strip()
# title case (captalizes the first letter of each word)
print(text.title()) 
# Upper case (capitalizes all letters)
text= text.upper()
print(text)
# Lower case (converts all letters to lower case)
text= text.lower()
print(text)
#count the number of characters in the string
print("Number of characters in the string: ", len(text))
#count the number of words in the string
print("Number of words in the string: ", len(text.split()))
#replace a string 
print(text.replace("imcc", "IMCC"))
#check if a string starts with a specific substring
print(text.startswith("welcome"))   
#check if a string ends with a specific substring
print(text.endswith("imcc"))    
#split a string into a list of substrings based on a delimiter
print(text.split(" "))  
#join a list of strings into a single string with a specific delimiter
words = ["welcome", "to", "imcc"]
print(" ".join(words))


