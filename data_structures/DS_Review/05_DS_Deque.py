#in BFS(Breadth-first search) or other algorithms where we have to pop or
# add elements to the begining , deque is the best option
#we can also use list, but list.pop(0) is O(n) operation where as dequeu.popleft() is O(1)

from collections import deque

queue = deque(['name','age','DOB'])

queue.append("append_from_right") # Append from right
queue.pop() # Pop from right

queue.appendleft("fromLeft") # Append from left
queue.popleft() # Pop from left

queue.index(element,begin_index,end_index) # Returns first index of element b/w the 2 indices.
queue.insert(index,element)
queue.remove() # removes first occurrance
queue.count() # obvious

queue.reverse() # reverses order of queue elements