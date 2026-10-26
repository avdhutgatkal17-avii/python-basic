#create a list of 10 numbers and display the sum of last 4 elements
#remove the items from the list located at 2 & 5 positions
#print the difference between the largest and smallest numbers in the list
#append a new element in a list which is half of the item located at 3rd position

numbers = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100]
print(" The sum of Last 4 elements in the list is :", sum(numbers[-4:]))

#del numbers["2" , "5"]

print("remove the items from position 2 &b 5 in the list",numbers.pop(2), numbers.pop(5))
print("",numbers)

print("The difference between the largest and smallest numbers in the list is:", max(numbers) - min(numbers))


numbers.append(numbers[2] / 2)
print("The list after appending the new element is:", numbers)


