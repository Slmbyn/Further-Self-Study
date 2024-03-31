# from ...BinaryTree import Node, BinaryTree
import binary_tree

# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.left = None
#         self.right = None
        
# class BinaryTree:
#     def __init__(self) -> None:
#         self.root = None
        
#     def insert(self, data):
#         self.root = self.insert_recursively(self.root, data)
        
#         # new_node = Node(data)
#         # if self.root == None:
#         #     self.root = new_node
#         # else:
#         #     self.insert_recursively(self.root, new_node)
    
#     def insert_recursively(self, root, data):
#         if root is None:
#             return Node(data)
#         elif data < root.data:
#             root.left = self.insert_recursively(root.left, data)
#         elif data > root.data:
#             root.right = self.insert_recursively(root.right, data)
#         return root

def preOrderTraversal(root):
    '''Pass in the root node of the Tree & will print in Root->Left->Right'''
    result = []
    if root:
        result.append(root.data)
        result.extend(preOrderTraversal(root.left))
        result.extend(preOrderTraversal(root.right))
    return result

def inOrderTraversal(root):
    '''Pass in the root node of the Tree & will print in Left->Root->Right'''
    result = []
    if root:
        result.extend(inOrderTraversal(root.left))
        result.append(root.data)
        result.extend(inOrderTraversal(root.right))
    return result

def postOrderTraversal(root):
    '''Pass in the root node of the Tree & will print in Left->Right->Root'''
    result = []
    if root:
        result.extend(postOrderTraversal(root.left))
        result.extend(postOrderTraversal(root.right))
        result.append(root.data)
    return result

if __name__ == "__main__": #If this file is imported by another, the code inside this if block will not execute if the file that imported it was directly executed
    treeExample = binary_tree.BinaryTree()
    treeExample.insert(13)
    treeExample.insert(2)
    treeExample.insert(3)
    treeExample.insert(33)
    treeExample.insert(53)
    treeExample.insert(4)
    treeExample.insert(1)
    
    print('preorder')
    print(preOrderTraversal(treeExample.root))
    print('inorder')
    print(inOrderTraversal(treeExample.root))
    print('postorder')
    print(postOrderTraversal(treeExample.root))