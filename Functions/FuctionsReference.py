__author__ = 'ugunipati'

def changeme(mylist):
    mylist.append([1,2,3,4])
    print 'Inside a function', mylist
    return

mylist = [10,1,2,11]
changeme(mylist)


# Outside the function it is a global variable whatever the values assigned that will be seen outside the function even after assiging it to the inside a function
def changeme( mylist ):
    "This changes a passed list into the function"
    mylist = [1,2,3,4]
    print "Values inside the function", mylist

mylist = [10,20,30]
changeme(mylist)
print "Outside the functions", mylist

#Keyword arguments

changeme ( mylist = [1,2,3])
print "Outside the functions", mylist



