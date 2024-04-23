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
    
    def insert_recursively(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert_recursively(root.left, data)
        elif data > root.data:
            root.right = self.insert_recursively(root.right, data)
        return root
    
    def search(self,target):
        return self.search_recursive(self.root, target)
        
    def search_recursive(self, root, target):
        # compare target with root
        if root is None or root.data == target:
            return root

        # search the left subtree   
        elif target < root.data:
            return self.search_recursive(root.left, target)
            pass
        
        # search the right subtree
        elif target > root.data:
            return self.search_recursive(root.right, target)
            pass

        return 'Not Found'
    
    def delete(self, target):
        return self._delete_recursive(self.root, target)

    def _delete_recursive(self, root, target):
        if root is None:
            return None  # Node not found

        # recursively search for the target node
        if target < root.data:
            root.left = self._delete_recursive(root.left, target)
        elif target > root.data:
            root.right = self._delete_recursive(root.right, target)
        else: # Node with target value found
            # If it has no children:
            if not root.left and not root.right:  
                return None # Sets the data value of the target node the value of None
            # If it only has a right child
            if root.left is None: 
                return root.right  # Replace node with its right child
            # If it only has a left child
            elif root.right is None: 
                return root.left  # Replace node with its left child
            else:
                # If node has both children
                
                #find the node with the minimum value 
                successor = root.right # Go down the right side
                while successor.left: # Keep going left until you find the last one (minimum value)
                    successor = successor.left
                
                # Swap the target node's data with that of the minimum      (effectively: give target node the min value data, then go give the min value node a value of None)
                root.data = successor.data #gives the targeted node, the value of the min node
                root.right = self._delete_recursive(root.right, successor.data) #find and delete the min node(by giving it a value of None), since it's value has now replaced the targeted node (we dont want it duplicated)

        return root

    
    def tree_rotation():
        pass
    
print('binary_tree.py just got executed entirely')