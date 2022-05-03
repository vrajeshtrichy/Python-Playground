import Visualising_Doubly_LinkedLists as Dll

# # Definition for a Node.
# class Node(object):
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child


def flatten(head):
    """
    :type head: Node
    :rtype: Node
    """
    return head

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

# Example to show usage
array = [1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12]
head = Dll.makeLists(array)
Dll.printLists(head)




# PYTHON RECURSION
# def flatten(self, head: 'Node') -> 'Node':
#     def dfs(node):
#         if not node:
#             return None, None
#         trav = node
#         head = node
#         tail = node
#         while trav:
#             if trav.child:
#                 nex = trav.next
#                 insert, last = dfs(trav.child)
#                 trav.next = insert
#                 insert.prev = trav
#                 if nex:
#                     last.next = nex
#                     nex.prev = last
#                 trav.child = None
#                 trav = last
#             tail = trav
#             trav = trav.next
#         return head, tail
#
#     return dfs(head)[0]