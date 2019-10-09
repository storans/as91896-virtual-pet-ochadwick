SUPER_AGE = 65

keep_going = ""

while keep_going == "":
    age = input("What is your age?")
    if age >= SUPER_AGE:
        print("You get super")
    else:
        print("No super for you")
    keep_going = input("continue? press enter or q")
