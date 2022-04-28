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
        self.stackArr = []
        self.length = 0

    def peek(self):
        if self.length > 0:
            return self.stackArr[self.length-1]
        return None

    def push(self, value):
        self.stackArr.append(value)
        self.length += 1
        return self

    def pop(self):
        if self.length > 0:
            holdingNode = self.stackArr[self.length-1]
            del self.stackArr[self.length-1]
            return holdingNode
        return None

    def isEmpty(self):
        return True if self.length == 0 else False

    def printt(self):
        for ele in self.stackArr:
            print(ele, end=' ')
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
