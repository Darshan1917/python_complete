# we can create a empty list and use it later
# list_empty =  []        how it is done
# RANGE function in python

number = [1,2,3,4,5,6,7,8,9]
print (number)


# usage of range   # *****Usage list ( range( start value , end value , step )
num = list(range(1,20,2))
print (num)

# NOTE it doesnt inculde the end value that is specified
num1 = list(range(0,10))   # default step size is 1
print (num1)

num3 = list(range(len(number)))
print (num3)
