# print square of all numbers
for num in range(0, 10):
    print(num ** 2)

# print sum of all even numbers
sum = 0
for num in range(0, 10):
    if num % 2 == 0:
        sum = sum + num
print("Sun of even numbers is: %d" % sum)


# program to read 3 numbers (a, b, c), check how many numbers between a and b are divisible by c
def calculate(a, b, c):
    counter = 0
    for num in range(a, b):
        if num % c == 0:
            counter = counter + 1
    print("There are %d numbers that are divisible by %d between %d and %d" % (counter, c, a, b))


calculate(10, 20, 5)
