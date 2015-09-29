__author__ = 'ugunipati'


#Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]).
# To some extent, lists are similar to arrays in C. One difference between them is that all the items belonging to a list can be of different data type.
# The values stored in a list can be accessed using the slice operator ( [ ] and [ : ] ) with indexes starting at 0 in the beginning of the list and working their way to end -1.
# The plus ( + ) sign is the list concatenation operator, and the asterisk ( * ) is the repetition operator. For example:

# For example:

list=[1,2,3,4]
tinylist=[5,6,'python',1.0,1111111111111111111L]

#ist = list + tinylist

list[0]=5
list[1]=5
list[2]=5
list[3]=5

print list
print list[1]
print list[2:4]
print list[2:]
print list * 3
print list + tinylist

del list[0]
print list
