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

# if __name__ == "__main__":
#     linked_list = LinkedList()
#     linked_list.insert(4)
#     linked_list.insert(1)
#     linked_list.insert(3)
#     linked_list.insert(8)

#     linked_list.print_list()
#     linked_list.delete_by_key(1)
#     linked_list.print_list()





"""-------------------------------------------LINKEDIn LEARNING FOLLOW ALONG-----------------------------------------------"""



# SINGLY LINKED LIST NODE
class SLLNode:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        """
        Repr stands for representation
        This method returns a printed representation of whatever object we call it on
        Here we are overriding that method with our own code
        We dont have to attach this to an object directly, when something is being returned/printed, this happens behind the scenes
        """
        return "SLLNode object: data={}".format(self.data)
    
    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next

# SINGLY LINKED LIST
class SLL:
    def __init__(self):
        self.head = None
        
    def __repr__(self) -> str:
        return f"SLL object: head={self.head}"
    
    def is_empty(self):
        '''Will return True if there is no head node (is empty). False if there is a head node (not empty)'''
        return self.head is None
    
    def add_front(self, new_data):
        '''Add a node whose data is the new_data argument to the front of the Linked List'''
        # create a new node with the data passed in
        temp = SLLNode(new_data)
        # set that nodes pointer to the current head node
        temp.set_next(self.head)
        # make the new node set as the new head
        self.head = temp
    
    def size(self):
        ''' 
        Traverses the Linked List and returns an integer representing the number of nodes in the list.
        Time Complexity = O(n)
        '''
        size = 0
        if self.head is None:
            return size
        
        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()
            
        return size
    
    def search(self, data):
        '''
        Traverses the Linked List and returns True if the data searched for is present in one of the Nodes. 
        Otherwisem it returns False.
        Time Complexity: O(n)
        '''
        if self.head is None:
            return "linked list is empty. No nodes to search."
        
        current = self.head
        while current is not None:
            # The nodes data matches what we're looking for
            if current.get_data() == data:
                return True
            # The nodes data doesnt match
            else:
                current = current.get_next()
        # Return False if the while loop doesn't find what we're looking for
        return False
    
    def remove(self, data):
        '''
        Removes the first occurence of a Node that contains the data argument as its self.data variable. Returns Nothing.
        Time Complexity: O(n)
        '''
        
        # Handling an attempt to remove a node when a linked list is empty
        if self.head is None:
            return "Linked List is empty. No nodes to remove."
        
        # Whatever the value of 'current' is after the while loop, is the node to be deleted
        current = self.head
        previous = None
        found = False
        
        while not found:
            # Handling the case of finding the node that we want to remove
            if current.get_data() == data:
                found = True
            else:
                # Handling the case of getting to the tail & not having found the node we were looking for
                if current.get_next() == None:
                    return "A Node with that data value is not present."
                # Handling the case of moving to the next node
                else:
                    previous = current
                    current = current.get_next()
                    
        # Handles the deletion after node is found
        if previous is None:
            # Handling the case of if the node we're removing is the head node (would need to make the next node the new head node)
            # The head node has no pointer pointing to it, so by setting a new head node, the old one is gone/lost
            self.head = current.get_next()
        else:
            # If the node being deleted is not the head node, we need to make it so that the targeted node does not have any pointers
            # pointing at it.
            previous.set_next(current.get_next())
    
    def print_list(self):
        
        # Handling an attempt to remove a node when a linked list is empty
        if self.head is None:
            return "Linked List is empty. No nodes to print."
    
        current_node = self.head
        print("Linked List Elements: ", end="")
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# DOUBLY LINKED LIST NODE
class DLLNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
    
    def __repr__(self):
        """
        Repr stands for representation
        This method returns a printed representation of whatever object we call it on
        Here we are overriding that method with our own code
        We dont have to attach this to an object directly, when something is being returned/printed, this happens behind the scenes
        """
        return "DLLNode object: data={}".format(self.data)
    
    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data
    
    def get_next(self):
        return self.next
    
    def get_previous(self):
        return self.previous
    
    def set_next(self, new_next):
        self.next = new_next
        
    def set_previous(self, new_previous):
        self.previous = new_previous
    


class DLL:
    def __init__(self):
        self.head = None
        
    def __repr__(self) -> str:
        return 'DLL object: head='.format(self.head)
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        ''' 
        Traverses the Linked List and returns an integer representing the number of nodes in the list.
        Time Complexity = O(n)
        '''
        size = 0
        if self.head is None:
            return size
        
        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()
            
        return size
    
    def search(self, data):
        '''
        Traverses the Linked List and returns True if the data searched for is present in one of the Nodes. 
        Otherwisem it returns False.
        Time Complexity: O(n)
        '''
        if self.head is None:
            return "linked list is empty. No nodes to search."
        
        current = self.head
        while current is not None:
            # The nodes data matches what we're looking for
            if current.get_data() == data:
                return True
            # The nodes data doesnt match
            else:
                current = current.get_next()
        # Return False if the while loop doesn't find what we're looking for
        return False
    
    def add_front(self, new_data):
        '''Add a node whose data is the new_data argument to the front of the Linked List'''
        # create a new node with the data passed in
        temp = DLLNode(new_data)
        # set that nodes pointer to the current head node
        temp.set_next(self.head)
        # if the DLL already has a head, give that head a previous pointer
        if self.head is not None:
            self.head.set_previous(temp)
        # make the new node set as the new head
        self.head = temp
    
    def remove(self, data):
        '''Removes the first occurence of the data argument passed in. Time Complexity = O(n)'''
    # Edge Cases:
        # Target data is a middle node
        # Target data is the last node
        
        # 1) Remove a node from an empty list
        if self.head is None:
            return "Linked List Is Empty. No Nodes to Remove"
        
        current = self.head
        previous = current.get_previous()
        found = False
        
        while not found:
            if current.get_data() == data:
                found = True
            else:
                # 2) Target data to be removed isn't in the list
                if current.get_next() is None:
                    return "A node with that data value is not present"
                else:
                    current = current.get_next()
        
        # 3) Target data is the first node
        if current.previous is None:
            self.head = current.get_next()
            self.head.set_previous(None)
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())
                
            
        
sll = SLL()
sll.add_front('cheese')
sll.add_front('cat')
print(sll.search('cheese'))
sll.print_list()
