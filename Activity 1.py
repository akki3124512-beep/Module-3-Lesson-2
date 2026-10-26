bill = int(input("Enter your total bill: "))
tip = int(input("Enter the percentage you wanna tip your waiter: "))

def money(a, b):
     c = ((a/100)*b)
     return a + c

print("The amount of your tip is: ", money(bill, tip))