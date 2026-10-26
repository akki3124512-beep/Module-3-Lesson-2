fact = int(input("Enter the number you want to find the factorial of: "))
def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a*factorial(a-1)

print(f"The factorial of {fact} is: ", factorial(fact))
