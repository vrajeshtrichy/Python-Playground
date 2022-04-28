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

    # def __str__(self):
    #     return "<Value: " + str(self.value) + " Next: " + str(self.next) + ">"


class LinkedList:
    def __init__(self, value):
        # self.head = {
        #     'value': value,
        #     'next': None
        # }
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        # nextObj = {
        #     'value': value,
        #     'next': None
        # }
        nextObj = Node(value)
        self.tail.next = nextObj  # Adding new object to the existing tail
        self.tail = nextObj  # making the newObj as the tail
        self.length += 1
        return self

    def prepend(self, value):
        # self.head['next'] = self.head
        # self.head['value'] = value
        # self.length += 1
        # return self
        # nextObj = {
        #     'value': value,
        #     'next': None
        # }
        nextObj = Node(value)
        nextObj.next = self.head
        self.head = nextObj
        self.length += 1
        return self

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return self

        nextObj = Node(value)
        currentObj = self.head
        previousObj = None

        for i in range(index + 1):
            if currentObj.next is not None:
                if i == index:
                    # print(i, str(currentObj))
                    # print(i, str(previousObj))
                    nextObj.next = currentObj
                    previousObj.next = nextObj
                    self.length += 1
                else:
                    previousObj = currentObj
                    currentObj = currentObj.next
            else:
                nextObj.next = currentObj
                previousObj.next = nextObj
                self.length += 1
        return self

    def insert_better(self, index, value):
        if index == 0:
            return self.prepend(value)
        elif index >= self.length:
            return self.append(value)

        newNode = Node(value)
        leader = self.traverseTo(index - 1)
        follower = leader.next
        newNode.next = follower
        leader.next = newNode
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
            self.length -= 1
            return self
        leader = self.traverseTo(index - 1)
        follower = leader.next
        leader.next = follower.next
        self.length -= 1
        return self

    def reverse(self):
        if self.head.next is None:
            return self.head

        self.tail = self.head
        current = self.head
        prev = None
        while current is not None:
            # Choose the next new node
            next = current.next

            # Change the pointer of the current from next to previous
            # i.e. Reverse the pointer direction
            current.next = prev
            # Bucket the Nodes under Prev
            prev = current
            # Make the next node as the current node
            current = next
        self.head = prev




        # first = self.head
        # second = self.head.next

        # prev = None
        # current = self.head
        # while current is not None:
        #     next = current.next
        #
        #     current.next = prev
        #     prev = current
        #     current = next
        # self.head = prev

    def printt(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print('\nLength ' + str(self.length) + '\n')
    #
    # def __str__(self):
    #     return "Head: " + str(self.head) + "\nTail: " + str(self.tail) + "\nLength: " + str(self.length)


myLinkedList = LinkedList(10)
# print(myLinkedList)
myLinkedList.append(5)
myLinkedList.append(16)
# print(myLinkedList)
myLinkedList.prepend(4)
# print(myLinkedList)
myLinkedList.insert_better(3, 99)
# print(myLinkedList)
myLinkedList.remove(4)
myLinkedList.printt()
myLinkedList.reverse()
myLinkedList.printt()
