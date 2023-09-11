class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_level_order_recursive(value, self.root)
    
    def _insert_level_order_recursive(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_level_order_recursive(value, node.left)            
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_level_order_recursive(value, node.right)    

    def show_pre_order(self):
        if self.root is None:
            print('The tree is empty.')
        else:
            self.show_pre_order_recursive(self.root)

    def show_pre_order_recursive(self, node):
        print(node.value, end=' ')
        if node.left is not None:
            self.show_pre_order_recursive(node.left)
        if node.right is not None:
            self.show_pre_order_recursive(node.right)

    def is_valid_bst(self):
        if self.root is not None:
            return self._is_valid_bst(self.root, float('-inf'), float('inf'))
        return True  # An empty tree is considered a valid BST

    def _is_valid_bst(self, node, min_val, max_val):
        if node is None:
            return True
        if min_val < node.value < max_val:
            return (self._is_valid_bst(node.left, min_val, node.value) 
                    and self._is_valid_bst(node.right, node.value, max_val))
        else:
            return False

def insert():
    tree = BinaryTree()
    
    num = int(input('How many values do you want to insert? '))
    for i in range(num):
        value = int(input(f'Enter the {i+1}º value: '))
        tree.insert_level_order(value)
    print('Values inserted successfully.')
    tree.show_pre_order()
    print()
    
    return tree

tree = insert()
    
if tree.is_valid_bst():
    print("The tree is a valid binary search tree.")
else:
    print("The tree is not a valid binary search tree.")
