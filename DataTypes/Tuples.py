__author__ = 'ugunipati'

# tuples

#A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas.
# Unlike lists, however, tuples are enclosed within parentheses.
# The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed,
# while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists. For example:

tuple = (1,2,3,4)
tuple1 = (5,6,7,'test')

print tuple
print tuple[0]
print tuple[1:]
print tuple[1:4]
print tuple * 2
print tuple + tuple1
