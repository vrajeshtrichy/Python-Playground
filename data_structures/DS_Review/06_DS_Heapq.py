import heapq # (minHeap by Default)

nums = [5, 7, 9, 1, 3]

heapq.heapify(nums) # converts list into heap. Can be converted back to list by list(nums).
heapq.heappush(nums,element) # Push an element into the heap
heapq.heappop(nums) # Pop an element from the heap
# heappush(heap, ele) :- This function is used to insert the element mentioned
# in its arguments into heap. The order is adjusted, so as heap structure is
# maintained.
# heappop(heap) :- This function is used to remove and return the smallest
# element from heap. The order is adjusted, so as heap structure is maintained.

# Other Methods Available in the Library
# Used to return the k largest elements from the iterable specified
# The key is a function with that accepts single element from iterable,
# and the returned value from that function is then used to rank that element in the heap
heapq.nlargest(k, iterable, key = fun)
heapq.nsmallest(k, iterable, key = fun)


#Max heap in python

#By default heapq in python is min heap,
#if we want to use max heap we can simply invert the value of the keys and use heapq.
#For example, turn 1000.0 into -1000.0 and 5.0 into -5.0.

#The easiest and ideal solution
#Multiply the values by -1

#All the highest numbers are now the lowest and vice versa.

#Just remember that when you pop an element to multiply it with -1 in order to get the original value again.

#Example:

import heapq
heap = []
heapq.heappush(heap, 1*(-1))
heapq.heappush(heap, 10*(-1))
heapq.heappush(heap, 20*(-1))
print(heap)

The output will look like:

[-20, -1, -10]

#when popping element multiply it with -1

max_element = -heapq.heappop(heap)
print(max_element)