class Node:
    def __init__(self, val=-1):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = Node()

    def get(self, index: int) -> int:
        temp = self.head.next
        i = 0
        while temp and i != index:
            temp = temp.next
            i += 1
        if temp:
            return temp.val
        return -1

    def addAtHead(self, val: int) -> None:
        temp = self.head.next
        newnode = Node(val)
        self.head.next = newnode
        newnode.next = temp

    def addAtTail(self, val: int) -> None:
        temp = self.head
        while temp.next:
            temp = temp.next
        newnode = Node(val)
        temp.next = newnode

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head
        i = 0
        while temp and i != index:
            temp = temp.next
            i += 1
        if not temp or i < index:
            return
        nxt = temp.next
        newnode = Node(val)
        temp.next = newnode
        newnode.next = nxt

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        i = 0
        while temp.next and i != index:
            temp = temp.next
            i += 1
        if not temp.next or i < index:
            return
        temp.next = temp.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
