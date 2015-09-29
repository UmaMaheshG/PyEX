__author__ = 'ugunipati'

# Function is defined here.

def printstr(str):
    print "This is a print statement function: ", str;
    return;

# Calling a function
printstr('Python Code')


# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return;

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist


# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assign new reference in mylist
   print "Values inside the function: ", mylist
   return;

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist


# Function is defined here.

def printstr(str):
    print "This is a print statement function: ", str;
    return;

# Calling a function
printstr(str = 'Python Code')

if __name__=='__main__':
    print('example')