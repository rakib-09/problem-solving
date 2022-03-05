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
        if self.head is None:
            self.head = node
            return
        itr = self.head

        while itr.next:
            itr = itr.next
        itr.next = node

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
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(6)
    ll.removeDuplicatesFromLinkedList()
    ll.print_ll()
