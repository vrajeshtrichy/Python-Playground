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
        self.previous = None
        self.value = value
        self.next = None


class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newObj = Node(value)
        newObj.previous = self.tail
        self.tail.next = newObj
        self.tail = newObj
        self.length += 1
        return self

    def prepend(self, value):
        newObj = Node(value)
        newObj.next = self.head
        self.head.previous = newObj
        self.head = newObj
        self.length += 1
        return self

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        elif index >= self.length:
            return self.append(value)

        newNode = Node(value)
        leader = self.traverseTo(index - 1)
        follower = leader.next
        newNode.next = follower
        follower.previous = newNode
        leader.next = newNode
        newNode.previous = leader
        self.length += 1
        return self

    def traverseTo(self, index):
        counter = 0
        currentNode = self.head
        while counter != index:
            currentNode = currentNode.next
            counter += 1
        return currentNode

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.head = None
            self.length -= 1
            return self
        leader = self.traverseTo(index - 1)
        follower = leader.next
        nextNode = follower.next
        leader.next = nextNode
        nextNode.previous = leader

        self.length -= 1
        return self

    def printt(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print('\nLength ' + str(self.length)+'\n')


myLinkedList = DoublyLinkedList(10)
myLinkedList.printt()
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.printt()
myLinkedList.prepend(4)
myLinkedList.printt()
myLinkedList.insert(3, 99)
myLinkedList.printt()
myLinkedList.remove(2)

myLinkedList.printt()
