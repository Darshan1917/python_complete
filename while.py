# while loop executes till the condition is met
# here we need to check the condition on every cycle

# basic
counter = 0
while(counter<=10):
    print (counter)
    counter+=1


# creating a check machine


def enterdetails():
    name = raw_input("Enter your name")
    password = raw_input("enter your password")
    if name == 'darshan' and password == 'darshan123':
        print ("valid User")
    else:
        print ("invalid user")


def enterguest():
    print ("your logged in as guest")


def exit():
    return False

print ("Hi Welcome to the website")
X = 0
while(X!=3):
    print ("please select the one from the below options")
    print ("1 to enter the portal")
    print ("2 to be guest")
    print ("3 to exit ")
    X = input("Select an option")
    if X == 1:
        enterdetails()

    elif X==2:
        enterguest()

    elif X==3:
        exit()

    else:
        print("enter a valid number")


