# 1. print tables of all odd numbers from 1 to 10
count = 1 
n = 0

for i in range(1,11):
 if(i % 2 != 0):
    for j in range(1,11):
      print(i * j)
    print()  