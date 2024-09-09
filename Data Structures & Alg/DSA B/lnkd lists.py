class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def remove_first(self):
        if self.head is None:
            raise ValueError("List is empty")
        self.head = self.head.next
        self.size -= 1

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Uso do LinkedList
ll = LinkedList()
ll.add_last(10)
ll.add_last(20)
ll.add_last(30)
ll.print_list()
ll.remove_first()
ll.print_list()
