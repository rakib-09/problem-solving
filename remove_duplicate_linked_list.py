# This is an input class. Do not edit.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        node = Node(value, None)
        if self.head:
            node.next = self.head
        self.head = node

    def insert_at_end(self, value):
        node = Node(value, None)
        if self.head is None:
            self.head = node
            return
        itr = self.head
        while itr and itr.next:
            itr = itr.next
        itr.next = node

    def insert_at_key(self, value, key):
        itr = self.head
        for i in range(key - 1):
            if itr and itr.next:
                itr = itr.next
        node = Node(value, None)
        node.next = itr.next
        itr.next = node

    def delete_from_beginning(self):
        if self.head:
            self.head = self.head.next

    def delete_from_end(self):
        itr = self.head
        while itr and itr.next.next:
            itr = itr.next
        itr.next = None

    def removeDuplicatesFromLinkedList(self):
        itr = self.head
        while itr.next:
            if itr.value == itr.next.value:
                itr.next = itr.next.next
            itr = itr.next

    def print_ll(self):
        itr = self.head
        res = ''
        while itr:
            res += str(itr.value) + '-->'
            itr = itr.next
        print(res)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(5)
    ll.insert_at_key(6, 3)
    ll.print_ll()
    ll.delete_from_beginning()
    ll.delete_from_end()
    # ll.insert_at_end(66)
    # ll.insert_at_end(55)
    # ll.insert_at_end(44)
    # ll.insert_at_end(22)
    # ll.removeDuplicatesFromLinkedList()
    ll.print_ll()
