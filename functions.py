# here we are working with functions

def my_fun(greet):
    return '{} how are you '.format(greet)


X= my_fun('darshan')
print (X.upper())


# Defaulting the value in the function
def my_fun1(greet, names = 'master'):
    return '{} {}'.format(greet,names)

name = input('your name please')
greet = input('What do you what to be called ')
Y = my_fun1(greet,name)
print (Y.upper())

# passing one function inside another function

def add(a,b):
    c = a+b
    return c

def squ(x):
    res = x * x;
    return res

print ("enter the numbers you want to add and multiply")
num = input("first number")
num2 = input("second number")

output = squ(add(num,num2))
print (output)
