
# for superanuation, its a constant bc its not changed in the program
SUPER_AGE = 65
#a loop testing the different values
keep_going = ""

while keep_going == "":
    age = input("What is your age?")
    #must be greater than or equal for 65
    if age >= SUPER_AGE:
        print("You get super")
    else:
        print("No super for you")
    keep_going = input("continue? press enter or q")
