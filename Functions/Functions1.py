__author__ = 'ugunipati'


def printinfo(name, age):
    print "This is a function to call send the parameters"
    print "Name: ", name
    print "Age:", age
    return;
printinfo('Python', 2)
printinfo('Python Code', 3)
printinfo(name='PythonCode', age=4)



def functionreturn(num1, num2):
    num = num1 + num2
    print num;
functionreturn(1, 2)



num = 0
def functionreturn(num1, num2):
    num = num1 + num2
    print "Inside the function global num : ", num
    return num;

functionreturn(1, 2)
print "Outside the function global num : ", num