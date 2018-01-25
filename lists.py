# list Examples and operations
names = ["darshan", "farid", "abu", "chirag"]  # string list
print (names)
ages = [24,25,26,27]         # numeric list
print (ages)
mixedlist = ["darshan", 24, 'blue', "python",2.5,24]  # mixed list
print (mixedlist)


# *******************list operations
# Count
value = names.count("farid")       # counts how many times the name or value is present
print (value)                      # we will get the value as 1
value1 = mixedlist.count(24)           # counts how many times the name or value is present
print (value1)                     # output will be 2 as there are 2 values of 24

# append We can only ad one argument using the append operator and we we try to add more it gives errors
names.append('malli')        # append_1 = names.append("malli",25) - gives error
print (names)                # ['darshan', 'farid', 'abu', 'chirag', 'malli'] added malli in the end

# NOTE ***** NEVER ASSIGN the list to a new list it comes as none output
# extend
names.extend(["james","roy"])    # both the values will get added to the original names list and will have james and roy in them
print (names)                    # ['darshan', 'farid', 'abu', 'chirag', 'malli', 'james', 'roy']

# insert
# same as the extend but here we can add the values where we need by choosing index value
names.insert(3,"reema")     # index starts from 0 and the 4th values is Reema
print (names)               # ['darshan', 'farid', 'abu', 'reema', 'chirag', 'malli', 'james', 'roy']

# pop
# it is used for deletion operation
# default removal from the list is from last
# we can even specify the value

names.pop()    # default the last value is deleted that is roy is deleted
print (names)  # ['darshan', 'farid', 'abu', 'reema', 'chirag', 'malli', 'james']

names.pop(2)   # second index value is deleted abu
print (names)  # ['darshan', 'farid', 'reema', 'chirag', 'malli', 'james']


# Reverse
# it is used to reverse a list
names.reverse()                 # the values here gets reversed
print (names)                   # ['james', 'malli', 'chirag', 'reema', 'farid', 'darshan']


# length and index values
found = names.index("farid")   # farid is present at 4th index values and hence we got 4
print (found)                  # 4

print(len(names))    # very useful to find the length of the list we can use this in for loop in future
