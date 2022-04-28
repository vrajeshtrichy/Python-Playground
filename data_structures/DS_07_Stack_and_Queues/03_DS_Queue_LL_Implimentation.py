# myStack = {
#     'top': {
#         'value': 'Google',
#         'next':{
#             'value': 'Youtube',
#             'next': {
#                 'value': 'Udemy',
#                 'next': None
#             }
#         }
#     }
# }

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.first is not None:
            return self.first.value
        return None

    def enqueue(self, value):
        newNode = Node(value)
        if self.first is None:  # Or if length == 0
            self.first = newNode
            self.last = self.first
        else:
            self.last.next = newNode
            self.last = self.last.next
        self.length += 1
        return self

    def dequeue(self):
        if not self.first:
            return None
        holdingNode = self.first
        self.first = self.first.next
        self.length -= 1
        if self.length == 0:
            self.last = None  # IMPORTANT this is like the tail
        return holdingNode.value

    def isEmpty(self):
        return True if self.length == 0 else False

    def printt(self):
        temp = self.first
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print('\nLength ' + str(self.length) + '\n')


myQueue = Queue()
myQueue.printt()
print('isEmpty: ', myQueue.isEmpty())
myQueue.enqueue('Google.com')
myQueue.enqueue('Youtube.com')
myQueue.printt()
print(myQueue.peek())
myQueue.enqueue('Udemy.com')
myQueue.printt()
print('popped', myQueue.dequeue())
myQueue.printt()
print('isEmpty: ', myQueue.isEmpty())
print('popped', myQueue.dequeue())
myQueue.printt()
print('popped', myQueue.dequeue())
myQueue.printt()
print('popped', myQueue.dequeue())
myQueue.printt()
