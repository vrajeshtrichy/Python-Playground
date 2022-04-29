# Recursive function with base case

def inception(counter):
    if counter > 3:
        print(counter)
        return 'Done'
    inception(counter + 1)
    return 'Here'


print(inception(0))

# During recursion the Stack gets lined up with the Recursion functions at every call. The return 'Done' is returned
# as a local return to the inception function, and after the stack pops all the inception function, it returns the
# final return statement return 'Here'
