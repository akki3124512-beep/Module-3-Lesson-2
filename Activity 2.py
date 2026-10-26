digit = int(input("Please enter a number that is divisble by 3: "))

def cube(a, b=3):
    return a ** b

if digit%3 == 0:
    print("The cube of your number is: ", cube(digit))
else:
    print("Your digit isn't divisible by 3.")