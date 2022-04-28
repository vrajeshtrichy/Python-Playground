obj1 = {'a': True}
obj2 = obj1
obj1['a'] = 'Hellloo'
del obj1
print(obj2)
# obj2 points to the location of obj1. So though ob1 is deleted, the pointer still exists
obj2 = 'hai'
print(obj2)
# automatic garbage collection in python deletes the previous reference
