class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Linkedlist consists of methods such as append, prepend, insert_after_node
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        cur = self.head

        while cur is not None:
            if prev_node == cur.data:
                new_node.next = cur.next
                cur.next = new_node
                break
            cur = cur.next

    def print_list(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


def main():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(15)
    ll.prepend(1)
    ll.prepend(2)
    ll.insert_after_node(10, 1000)
    ll.print_list()


if __name__ == "__main__":
    main()
