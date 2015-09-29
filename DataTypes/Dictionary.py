__author__ = 'ugunipati'

#Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs.' \
#A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.
#Dictionaries are enclosed by curly braces ( { } ) and values can be assigned and accessed using square braces ( [] ).

# For example:


dict = {}

dict[0]='Python'
dict['testing'] = 'software'

print dict['testing']
print dict[0]
print dict
print dict.keys()
print dict.values()