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


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top is not None:
            return self.top.value
        return None

    def push(self, value):
        newNode = Node(value)
        if self.bottom is None:  # Or if length == 0
            self.bottom = newNode
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

            # holdingNode = self.top
            # self.top = newNode
            # self.top.next = holdingNode
        self.length += 1
        return self

    def pop(self):
        if not self.top:
            return None
        holdingNode = self.top
        self.top = self.top.next
        self.length -= 1
        if self.length == 0:
            self.bottom = None  # IMPORTANT this is like the tail
        return holdingNode.value

    def isEmpty(self):
        return True if self.length == 0 else False

    def printt(self):
        temp = self.top
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print('\nLength ' + str(self.length) + '\n')


myStack = Stack()
myStack.printt()
print('isEmpty: ', myStack.isEmpty())
myStack.push('Google.com')
myStack.push('Youtube.com')
myStack.printt()
print(myStack.peek())
myStack.push('Udemy.com')
myStack.printt()
print('popped', myStack.pop())
myStack.printt()
print('isEmpty: ', myStack.isEmpty())
print('popped', myStack.pop())
myStack.printt()
print('popped', myStack.pop())
myStack.printt()
print('popped', myStack.pop())
myStack.printt()
