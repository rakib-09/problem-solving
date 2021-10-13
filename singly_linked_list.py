class Node:

    def __init__(self, item=None, next_node=None):
        self.item = item
        self.next_node = next_node


class SinglyLinkedList:

    def __init__(self, head=None):
        self.head = head

    def append_left(self, item):
        new_node = Node(item)
        new_node.next_node = self.head
        self.head = new_node

    def append_last(self, item):
        current = self.head
        if current:
            while current.next_node:
                current = current.next_node
            current.next_node = Node(item)
        else:
            self.head = Node(item)

    def insert(self, position, item):
        if position == 0:
            self.append_left(item)
            print("inserted at the first position")
        elif position == self.size():
            self.append_last(item)
            print("inserted at the last position")
        elif position > self.size():
            print('index out of range')
        else:
            current_head = self.head
            previous = current_head
            index = 0
            while current_head:
                if index != position:
                    previous = current_head
                    current_head = current_head.next_node
                    index += 1
                else:
                    new_node = Node(item, current_head)
                    previous.next_node = new_node
                    current_head = False
                    print(item, "inserted at ", position)

    def is_empty(self):
        if self.head:
            return False
        return True

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def index(self, item):
        current = self.head
        index = 0
        while current:
            if current.item == item:
                return index
            else:
                current = current.next_node
                index += 1
        return None

    def search(self, item):
        current = self.head
        while current:
            if current.item == item:
                return True
            else:
                current = current.next_node
        return False

    def pop_left(self):
        if self.is_empty():
            return None
        else:
            current = self.head
            item = current.item
            self.head = current.next_node
            del current
            return item

    def pop(self):
        if self.is_empty():
            return None
        else:
            current = self.head
            previous = None
            while current.next_node:
                previous = current
                current = current.next_node
            previous.next_node = None
            item = current.item
            del current
            return item

    def remove(self, item):
        if self.is_empty():
            return None
        else:
            current = self.head
            previous = None
            while current.item != item:
                previous = current
                current = current.next_node
            if current is None:
                return None
            elif previous is None:
                self.pop_left()
            else:
                previous.next_node = current.next_node
                item = current
                del current
                return item

    def print_list(self):
        if self.is_empty():
            return
        else:
            current = self.head
            print(current.item)
            while current.next_node:
                current = current.next_node
                print(current.item)
