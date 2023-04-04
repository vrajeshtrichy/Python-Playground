dict = {'a':1,'b':2,'c':3}

dict.keys() # returns list of keys of dictionary
dict.values() # returns list of values of dictionary
dict.get('a') # returns value for any corresponding key
dict.items() # returns [('a',1),('b',2),('c',3)]
dict.copy() # returns copy of the dictionary
# NOTE : items() Returns view object that will be updated with any future
# changes to dict
dict.pop(KEY) # pops key-value pair with that key
dict.popitem() # removes most recent pair added
dict.setDefault(KEY,DEFAULT_VALUE)
# returns value of key, if key exists, else default value returned
# If the key exist, this parameter(DEFAULT_VALUE) has no effect.
# If the key does not exist, DEFAULT_VALUE becomes the key's value. 2nd
# argument's default is None.
dict.update({KEY:VALUE})
# inserts pair in dictionary if not present, if present, corresponding value is
# overriden (not key)
# defaultdict ensures that if any element is accessed that is not present in
# the dictionary
# it will be created and error will not be thrown (which happens in normal dictionary)
# Also, the new element created will be of argument type, for example in the below line
# an element of type 'list' will be made for a Key that does not exist
myDictionary = defaultdict(list)