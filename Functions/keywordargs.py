__author__ = 'ugunipati'

#Keyword arguments
#Passing variables and values using keyword arguments

def changeme( mylist ):
    "This changes a passed list into the function"
    print "Values inside the function", mylist

changeme ( mylist = [1,2,3])



#!/usr/bin/python

# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print "Name: ", name;
   print "Age ", age;
   return;

# Now you can call printinfo function
printinfo( age=50, name="Python" );