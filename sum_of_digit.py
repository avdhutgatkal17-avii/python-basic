# 4.Print the sum of digits

digits = 12345
total = 0

while digits > 0:
    total += digits % 10
    digits //= 10

print("The sum of all digits is:", total)

