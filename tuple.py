# tuple is type of immutable datatype it is like list that is of fixed length
# NOTE : We use curve brackets for tuples ()

my_tup =  ("raj","ravi","veena",'rakesh')
my_tup1 = ('dar','dom')
print (my_tup)
# Uncomment and run and check
#my_tup += ('rockstar')  # when we try to add ('rockstar') to the tuple directly it wont get added throws error
                         # ('raj', 'ravi', 'veena', 'rakesh')
                         # File "C:/Users/dumapath/PycharmProjects/Demo/tuple.py", line 7, in <module>
                         # my_tup += 'veenawem'
                         # TypeError: can only concatenate tuple (not "str") to tuple
# WE CAN NEVER CHANGE A TUPLE
updated_tup = my_tup+my_tup1  # here when we add one tuple to another via concatenation it works
print (updated_tup)           # ('raj', 'ravi', 'veena', 'rakesh', 'dar', 'dom')


# NOTE ; tuple can perform operations that are similar to String operations
# we saw concat on the top - adding two tuples


#*********** Recurring : *************

rec_tuple = my_tup * 3
print ('rec_tuple = ', rec_tuple)

#************** Slicing
# NOTE indexing in python starts with 0
tup_sel = my_tup[0]    # select the index 0 value and when it checks in the tuple the value is raj
print ('tup_sel =', tup_sel)  #'tup_sel =', 'raj'

tup_sel2= my_tup[0:3]
print ('tup_sel2 =', tup_sel2)  #('raj', 'ravi', 'veena')

tup_sel3 = my_tup[-1]    # select the index -1 value and when it checks in the tuple the value is rakesh
print ('tup_sel3 =', tup_sel3)