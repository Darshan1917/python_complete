# In control statement we have If else , if elif else , FOr , While , break and continue

# Lets start wirh IF and If ELif and Else
# Taking input from the user and giving the desired result regarding the grades
Y = input("Enter you grade")
X = int(Y)
if (X>100):
    print ("Enter a proper Grade")
elif(X > 80):
    print ("Grade A")
elif(X>70):  # (X > 80) & (X<100):
    print ("Grade B")
elif(X>60):
    print ("Grade C")
else :
    print ("GO study")


Z = input("Is it raining")
if(Z=="Yes") or (Z=='yes') or (Z=='YES'):
    print ("Don't go out")
else:
    print ("GGOOOOO Out ")