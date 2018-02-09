# Accepting inputs from user
# for 2.7 we had raw_input but for 3.5 we dont have just give input
raw_input("Please enter a value ") #*******raw _input in 2.7 is for strings and only input is for numbers

# IN 3.5 current systems

input("whats your idea")          #************* Considers both for string and numeric values both are taken as string



#***************************** STRING Operation ************************************
# Immutable datatype
Fname = "Darshan"
Lname = 'Umapathi'
num_string = "5"
num2_string = "2"

# Concatenation  ************
# for concatenations we use + symbol joining of string
Full_name = Fname + Lname
print ("Full_name =", Full_name)
num_concat = num_string + num2_string
print ('num_concat =', num_concat) # num_concat = 52 output is not 7 but 52 concatenates here

#************** Recurring : same string has to be repeated multiple times then we need to use " * " symbol

Rec_fname = Fname * 5  # string * with interger not string with string
print ("Rec_fname =" , Rec_fname)

# ********Very IMP SLICING Operation
# NOTE : In python the index value starts from 0 and we need to use the syntax as string[start index : end index]

S_Fname = Fname[2:6]  # the range is with i the subjected range D A R S H A N           considered 2 but ignores 6
print ('S_Fname =', S_Fname)                                 #  0 1 2 3 4 5 6
                                                             # -7-6-5-4-3-2-1
S_Fname1 = Fname[0:6] # here selected from Zero 0 so we get all the values till 6 and excluide the 6 value
print ('S_Fname1 =', S_Fname1)
S_Fname2 = Fname[0:16] # the end value is larger than the string length ?? lets see what happens
print ('S_Fname2 =', S_Fname2)  # S_Fname2 = Darshan -- output it considers the length of the string and then coes out
S_Fname3 = Fname[-1:3]  # here i have given negative value lets check !!!! ( start value )
print ('S_Fname3 =', S_Fname3)   # S_Fname3 =      i got nothing as output hence doesnt considers the the negative start value
S_Fname4 = Fname[1:-3]       # negative end value
print ('S_Fname4 =', S_Fname4)   # S_Fname4 = ars   here we saw index 1 is a and index of -3 is H that is y it doesnt consdier it and
                               # selects the value less than that

# TYPE specfic functions on string values
# REMEMBER  CASE SENSITIVE
#**************** Find
# as the name suggest it finds the mini or sub string in a given whole string and return the starting index of the string
# NOTE : it returns the Index value

find = Fname.find('an') # String is darshan and an is the last 2 character lets see output
print ('find=', find )  # find= 5 it returned the index value of a that is 5
find2 = Lname.find('pat')
print ('find2=', find2)

# ****************  Replace
# here it replcaes the type of string with some other specified string

replace_f = Fname.replace('ar','zz') # here the first one is the self value and second one is the replaced value
print ('replace_f = ', replace_f)        # replace_f =  Dzzshan
replace_l = Lname.replace('hi','pk')
print ('replace_l =', replace_l)         # replace_l= Umapatpk


# ***************  split
# Used to split the string here we have specifiy the delimiter and its a coustom delimiter
# the delimiter can be ' , . ? \ / anything alphabet or numbers isdier a string
# NOte here output is a LIST

new_string = 'Darshan, is a good basketball player '
split_f1 = Fname.split('a')         # a is used as a delimiter
print ('split_f1 =' , split_f1) # split_f1 = ['D', 'rsh', 'n']
split_newstring = new_string.split(',')
print ('split_newstring = ', split_newstring)  # split_newstring =  ['Darshan', ' is a good basketball player'] Darshan is one list and remaining is one list

# *****************  count
# here it counts the number of times the character is there in present in the string
#We can also give start and end values

count_f = Fname.count('a')
print  ("count_f =" , count_f)   # count_f = 2 ; this is cuz a is present twice in darshan
count_l = Lname.count('i')
print ("count_l = ", count_l )   # count_l =  1  only once i is there in umapathi
count_l1 = Lname.count('1',0,4)
print ("count_l1 = ", count_l1)    # count_l1 =  0  here 0 because we have given the start (0) and end values(4) and in between them we didnt have any 'i'

# lets see a case sensitive example
count_l2 = Lname.count('I') # Do we have I or i in Umapathi based on this we will get output
print 'count_l2 =', count_l2  # count_l2 = 0     NO I be careful



# ************** upper and lower conversion

f_upper  = Fname.upper()    # convert the entire value to Upper case
print ('f_upper=', f_upper)   # f_upper= DARSHAN
f_lower = Fname.lower()     # lower case
print ('f_lower =', f_lower)  # f_lower = darshan

# ************** max and min operstaions
# finds the max value in a string  and min value

f_max = max(Fname) #checks in Fname = darshan the max value that is s and gives that as output
print ('f_max = ', f_max) #f_max =  s
f_min = min(Fname) #checks in Fname = darshan the max value that is s and gives that as output
print ('f_min = ', f_min) # f_min =  D in Darshan  value minimun is D and if we chnage drom Darshan to darshan we will get a NOTE Case sensitive
f_min_csae = min(Fname.lower()) # case chnaging to lower and checking output
print ('f_min_csae = ', f_min_csae) #f_min =  a -- as expected we get a small case

#************************* Explore other like by clicking Fname. **********************