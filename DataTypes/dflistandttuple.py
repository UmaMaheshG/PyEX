__author__ = 'ugunipati'


#Following is invalid with tuple, because we attempted to update a tuple, which is not allowed.
# Similar case is possible with lists:

# For example:

list = [1,2,3,4]
tuple=(1,2,3)

list[0]=5

print list

tuple[0]=5
print tuple