# mylikedlist = {
#     'head': {
#         'value': 10,
#         'next':{
#             'value': 15,
#             'next': {
#                 'value': 16,
#                 'next': None
#             }
#         }
#     }
# }

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "<Value: " + str(self.value) + " Next: " + str(self.next) + ">"


class LinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        nextObj = {
            'value': value,
            'next': None
        }
        self.tail['next'] = nextObj  # Adding new object to the existing tail
        self.tail = nextObj  # making the newObj as the tail
        self.length += 1
        return self

    def __str__(self):
        return "Head: " + str(self.head) + "\nTail: " + str(self.tail) + "\nLength: " + str(self.length)


myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
print(myLinkedList)

# OUTPUT
# Head: {'value': 10, 'next': {'value': 5, 'next': {'value': 16, 'next': None}}}
# Tail: {'value': 16, 'next': None}
# Length: 3
