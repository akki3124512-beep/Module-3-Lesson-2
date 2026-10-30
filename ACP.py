def shutdown(a):
    if a == "yes":
        return "shutting down now."
    elif a == "no":
        return "aborting shut down."
    else:
        return "sorry."

x = input("Do you want to shut down? \n Enter what you want to do: ")

print("Okay, we are", shutdown(x))

