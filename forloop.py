# Looping statement that can be used for replication
# They can also be used to get values from list when we access from database
# Syntax
# for x in range(1:10):
#       CODE
# NOTE : always in range the last value is not considered

for x in range(1,11):
    print(x)


# now let us try to access the list from the FOR loop

List = ["darshan", "farid", 'malli' , 'sathish' , 'raj', 'ravi']

for y in range(0,(len(List)/2)):
    print (List[y])
    print ("Hello")

# Second way of doing or executing the list is
kist1 = ["dars", "far", 'mai', 'sathi', 'rj', 'ra']
for c in kist1:
    print (c)

# code to print even number from 1 to 20

for x in range(1,21):
    if x%2 ==0:
        print (x)