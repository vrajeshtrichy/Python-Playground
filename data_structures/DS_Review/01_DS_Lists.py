nums = [1,2,3]

nums.index(1) # returns index
nums.append(1) # appends 1
nums.insert(0,10) # inserts 10 at 0th index
nums.remove(3) # removes all instances of 3
nums.copy(1) # returns copy of the list
nums.count(1) # returns no.of times '1' is present in the list
nums.extend(someOtherList) # ...
nums.pop() # pops last element [which element to pop can also be given as optional argument]
nums.reverse() # reverses original list (nums in this case)
nums.sort() # sorts list [does NOT return sorted list]
#Python's default sort uses Tim Sort, which is a combination of both merge sort and insertion sort.
