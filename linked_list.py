class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, val):
        node = Node(val, self.head)
        self.head = node

    def insert_at_end(self, val):
        node = Node(val, None)
        if self.head is None:
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node
        return

    def print(self):
        if self.head is None:
            print("no linked list")
        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.value) + '-->'
            itr = itr.next
        print(llist)


# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_at_beginning(5)
#     ll.insert_at_beginning(89)
#     ll.insert_at_end(49)
#     ll.print()
