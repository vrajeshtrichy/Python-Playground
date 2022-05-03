from DS_LinkedLists import LinkedList

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# THIS FAILS IN EDGE CASE -
# Head = [3,5]
# Left = 1
# Right = 2
def reverseBetween_bk(head, left, right):
    """
    :type head: ListNode
    :type left: int
    :type right: int
    :rtype: ListNode
    """
    currentPosition = 1
    currentNode = head
    start = head
    tail = None
    listSoFar = None
    while currentNode is not None:
        print('currentNode',currentNode.value)
        if currentPosition == left-1:
            start = currentNode
        if currentPosition == left:
            tail = currentNode
            while currentPosition in range(left, right+1):
                # print(currentNode.value)
                next = currentNode.next
                currentNode.next = listSoFar
                listSoFar = currentNode
                currentNode = next
                currentPosition += 1
                print('loop')
                printt(listSoFar)
            break
        currentNode = currentNode.next
        currentPosition += 1
    start.next = listSoFar
    tail.next = currentNode
    printt(listSoFar)
    printt(head)

    if left > 1:
        return head
    else:
        return listSoFar

def reverseBetween(head, left, right):
    start = head
    currentNode = head
    currentPosition = 1
    while currentPosition < left:
        start = currentNode
        currentNode = currentNode.next
        currentPosition += 1
    tail = currentNode
    newList = None
    while currentPosition >= left and currentPosition <= right:
        next = currentNode.next
        currentNode.next = newList
        newList = currentNode
        currentNode = next
        currentPosition += 1

    start.next = newList
    tail.next = currentNode

    if left > 1:
        return head
    else:
        return newList

def printt(head):
    temp = head
    while temp is not None:
        print(temp.value, end=' ')
        temp = temp.next
    print()

def strLists(head, lists):
  '''
  Helper function to recursively serialize the graph prior to visualization. It's an interim step and
  only meant to be called by the printLists function.

  Parameters:
    head - head of the present list
    lists - the serialization being built recursively (passed by reference)

  Returns:
    None (lists is updated in place).
  '''
  if head is None:
    return
  nodes = []
  while head:
    nodes.append(str(head.value))
    # if head.child is not None:
    #   nodes.append('|')
    #   strLists(head.child, lists)
    head = head.next
  lists.append(nodes)
def printLists(head):
  '''
  Visualizes the entire graph
  Parameter:
    head - the top most Node
  '''
  lists = []
  strLists(head, lists)
  if lists == []:
    print(None)
    return
  previndent = 0
  for j, l in enumerate(lists[::-1]):
    count = -1
    indent = 0
    s = []
    for i in range(len(l)):
      if l[i] != '|':
        s.append(l[i])
        count += 1
      else:
        indent = count * 4
        child = count
    print('---'.join(s))
    if  len(lists) > 1 and j < len(lists) - 1:
      previndent += indent
      indentation = ''.join([' '] * previndent)
      if len(l[0]) > 1:
        indentation += ''.join([' '] * child)
      print(indentation + '|')
      print(indentation, end='')

myLinkedList = LinkedList(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(5)

listHead = myLinkedList.head
printLists(listHead)
listHead = reverseBetween(listHead, 2, 4)
printLists(listHead)


myLinkedList2 = LinkedList(1)
myLinkedList2.append(2)

listHead2 = myLinkedList2.head
printLists(listHead2)
listHead2 = reverseBetween(listHead2, 1, 2)
printLists(listHead2)

