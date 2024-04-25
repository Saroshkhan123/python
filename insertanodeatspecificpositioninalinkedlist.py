#Insert a node at specific position in a linked list

def insertNodeAtPosition(llist, data, position):
   newNode = SinglyLinkedListNode(data)
   index = 0
   curr = llist
   prev = None
  
   while index != position:
       prev = curr
       curr = curr.next
       index += 1
      
   if prev == None:
       newNode.next = llist
       return newNode
  
   newNode.next = prev.next
   prev.next = newNode
   return llist
