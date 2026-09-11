age = int(input("Enter your age: "))
student = input("are you a student?, yes or no: ")
print("you are eligible for the discount:", age <= 21 and student == "yes")