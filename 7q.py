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

    def show_post_order(self):
        if self.root is None:
            print("The root is empty.")
        else:
            self.show_post_order_recursive(self.root)
        
    def show_post_order_recursive(self, node):
        if node.left is not None:
            self.show_post_order_recursive(node.left)
        if node.right is not None:
            self.show_post_order_recursive(node.right)
        print(node.value, end=' ')

# Example usage
tree = BinaryTree()
tree.insert_level_order(5)
tree.insert_level_order(3)
tree.insert_level_order(7)
tree.insert_level_order(2)
tree.insert_level_order(4)
tree.insert_level_order(6)
tree.insert_level_order(8)
print('Numbers in post-order: ')
tree.show_post_order()
print()
