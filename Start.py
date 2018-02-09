print 'Hello World!!!!'

# python is case sensitive
# Arithmatic Operations

#### Addition/Subtraction
Add1  =  5;
Add2  = -10;
Add_Final =  Add1+Add2;
print 'Add_Final =' , Add_Final;

Sub1 = 12+48
Sub2 = -43
Sub_final =  Sub1 - Sub2 ;
print 'Sub_final = ', Sub_final

#**************Short Cut to use for recursive addition/subtraction/Multiplication/String -INPLACE  Operator
Add2 += 2
Add1 -= 2
Sub1 *= 2
print (Add2);  #-8
print (Add1);  # 3
print (Sub1);  # 120

#********* Multiplication/Division/power/whole division and partial division
mul1 = 5
mul2 = 6
mul3 = 2
mul_final = mul1 * mul2
power = mul1 ** mul3
value = 49 ** (1/2)
print 'mul_final =',mul_final
print  'Power(5^2) =' , power
print  'sqaure =' , value

div1 = 17
div2 = 3

div_final = div1 / div2; # normal division with retuen of decimal values if there are any
print "div_final = " , div_final

div_final2 =  div1 // div2  # only intergers are returned
   #*******div_final_zero = 589 / 0 # Zero division error

print  "div_finals2 = ", div_final


#************* modulus _---  returns remainder after division -- check if the number is completely divided

mod1 = 10
mod2 = 7
mod3 = 2
mod_final1 =  mod1 % mod3 # 10/2 gives a remainder 0 -  completely divides
mod_final2 = mod1 % mod2 # 10/7 gives a remainder 3
print "mod_final1 =" , mod_final1 # Zero remainder
print  "mod_final2 = ", mod_final2 # non Zero value

# ******************* Comparision operators **********
# logical values are returned True or False
num1 = 100
num2 = 56
num3 = 156

print "num1 > num3 = " ,num1 > num2
print "num1 == num3 = " ,num1 ==  num3 # NOTE **** == for comparison if we use single = the it is to assign
print "num3 > num1 = " ,num3 > num1
print "num3 != num2 = " ,num3 != num2



