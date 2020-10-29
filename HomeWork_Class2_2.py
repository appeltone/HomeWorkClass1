# Exercise B
for i in range(10):
    print(i)

# Exercise C
number = 2
if (number == 1):
    print("Summer")
elif (number == 2):
    print("Winter")
elif (number == 3):
    print("Fall")
elif (number == 4):
    print("Spring")


# Exercise D
# 1. 10
# 2. 10

# Exercise F
phone = input("Enter your Phone number: ")
print(" Phone number | %s " % phone)


# Exercise I
def addNumbers(a, b):
    return a + b


print(addNumbers(2, 4))


def jopinStringsWthSpace(str1, str2):
    return "%s %s" % (str1, str2);


print(jopinStringsWthSpace("hello", "world"))

# # Challenge K
for i in range(10):
    for j in range(i+1):
        print('*', end=' ')
    print()

# Challenge L
width = 7
for i in range(width):
    for j in range(width):
        if (i-j == 0) or (i + j == width - 1) :
            print("*", end="")
        else:
            print(end=" ")
    print()

# Challenge M
def getNumFromUser():
    num = int(input("Please enter number for calculation: "))
    return num

def countDigits():
    num = getNumFromUser()
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10

    print("the number of digits in %d is %d" % (num, count))

countDigits()


