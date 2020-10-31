
while (True):
    num = int(input("Enter a number: \n"))
    try:
        if (num >= 0):
            break
        else:
            raise ValueError()
    except ValueError:
        print("number is negative, try again ")

print("Thank you. the number you provided is: %d " % num)
