# Write a python program to check given number is prime or not
numToCheck = int(input("Enter a number to check: "))
flag = 0

if (numToCheck == 2):
    print("Your num is PRIME")
else:
    for num in range(2, numToCheck - 1):
        if (numToCheck % num == 0):
            print("Your number is not PRIME")
            break
        else:
            print("Your number is PRIME")
            break


# Write a python program to print all prime numbers between 0 to 100 , and print
# how many prime numbers are there.
sumOfPrimes = 0
flag = True
for i in range(2, 100):
    flag = True
    for j in range(2, i):
        if (i % j == 0):
            flag = False
    if (flag == True):
        sumOfPrimes = sumOfPrimes + i
        print(i, end=" ")
