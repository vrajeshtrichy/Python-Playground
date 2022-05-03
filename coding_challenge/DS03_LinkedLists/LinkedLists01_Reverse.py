from DS_LinkedLists import LinkedList

def reverseSinglyLinkedList(head):
    if head.next is None:
        return head

    current = head
    listSoFar = None
    while current is not None:

        # Keep reference of the Next Node in the list
        next = current.next
        # >> next = Second
        # >> next = Third

        # Change the pointer of the current from next to previous
        # i.e. Reverse the pointer direction
        current.next = listSoFar
        # >> current.next = second
        # >> current.next = None
        # >> current.next = First
        # >> current.next = Second

        # Bucket the Nodes under Prev
        listSoFar = current
        # >> prev = None
        # >> prev = None, First
        # >> prev = None, First, Second

        # Make the next node as the current node
        current = next
        # >> current = Second
        # >> current = Third
        # >> current = Fourth

    return listSoFar

def printt(head):
    temp = head
    while temp is not None:
        print(temp.value, end=' ')
        temp = temp.next
    print()


myLinkedList = LinkedList(10)

myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(4)
myLinkedList.insert_better(3, 99)
myLinkedList.remove(4)

listHead = myLinkedList.head
printt(listHead)
listHead = reverseSinglyLinkedList(listHead)
printt(listHead)