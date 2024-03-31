class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        
    def insert(self, data):
        self.root = self.insert_recursively(self.root, data)
        
        # new_node = Node(data)
        # if self.root == None:
        #     self.root = new_node
        # else:
        #     self.insert_recursively(self.root, new_node)
    
    def insert_recursively(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert_recursively(root.left, data)
        elif data > root.data:
            root.right = self.insert_recursively(root.right, data)
        return root
    
    
print('binary_tree.py just got executed entirely')