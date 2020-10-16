# Question A
first = 7
second = 44.3
print(first + second)
print(first * second)
print(second / first)

# Question B
# a = 9
# c = 15
# b = 8

# Question C
# no difference , both are strings
# only matters if you have ' or " inside the string it self

# Question D
# 7 will be printed

# Question E
x = 5
y = 15
if x > y:
    print("Bigger")
elif x < y:
    print("Smaller")

# Question F
season = 2
if season == 1:
    print("Summer")
elif season == 2:
    print("Winter")
elif season == 3:
    print("Fall")
elif season == 4:
    print("Spring")

# Challenge
a = 8
b = "123"
print(a + int(b))

# extra exercises 1
num = 5
numStr = "5"
compareResult = (num == numStr)
sum = (num + int(numStr))
print(sum)
print(True == False)
print(5 > 5.5)
print("hello" > "helloo")

# extra exercises 2
name = input("Enter your name (first letter Capital please):")
while (not name[0].isupper()):
    name = input("Again BOZO... (first letter Capital please!):")
age = input("Enter your age:")
work = input("Enter your profession:")
print(" %s | %s | %s " % (name, age, work))


