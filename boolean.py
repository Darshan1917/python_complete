# boolean values are and or xor etc
# they are used to make multiple check options

# USER interface
username =  input("Enter the username")
password = input("Enter the password")


if username == 'admin' and password == "admin123":
    print ("Valid user")
else:
    print ("Invalid User ")