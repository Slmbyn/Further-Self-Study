# Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = None
        new_node.previous = None

        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                print("Traversing linked list...")
                last_node = last_node.next
            last_node.next = new_node
            new_node.previous = last_node

    def delete_by_key(self, key):
        print()
        print(f"Delete Element {key} from Linked List")
        current_node = self.head
        previous_node = None

        if current_node is not None and current_node.data == key:
            self.head = current_node.next
            print(f"{key} found and deleted")
            return

        while current_node is not None and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next

        if current_node is not None:
            previous_node.next = current_node.next
            print(f"{key} found and deleted")
        if current_node is None:
            print(f"{key} not found")

    def print_list(self):
        current_node = self.head
        print("Linked List Elements: ", end="")
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(4)
    linked_list.insert(1)
    linked_list.insert(3)
    linked_list.insert(8)

    linked_list.print_list()
    linked_list.delete_by_key(1)
    linked_list.print_list()
