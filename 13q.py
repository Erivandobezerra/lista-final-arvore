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

    def height(self):
        if self.root is None:
            return 0
        else:
            return self._height(self.root) 
    
    def _height(self, node):
        if node is None:
            return 0
        left_height = 0
        right_height = 0

        if node.left is not None:
            left_height = 1 + self._height(node.left)
        if node.right is not None:
            right_height = 1 + self._height(node.right)
        if left_height > right_height:
            return left_height
        else:
            return right_height
                
    def nodes_at_level(self, level):
        if self.root is None:
            print('The tree is empty.')
        else:
            height = self.height()
            if level > height:
                print()
                print('This level does not exist in the tree.')
            else:
                self._nodes_at_level(self.root, level, 0)
    
    def _nodes_at_level(self, node, level, current_level):
        if level == 0:
            print(node.value)
        elif node is not None:
            if level == current_level:
                print(node.value, end=' ')
            else:
                self._nodes_at_level(node.left, level, current_level + 1)
                self._nodes_at_level(node.right, level, current_level + 1)
                
def nodes_per_level():
    tree = BinaryTree()
    
    num = int(input('How many values do you want to insert in the tree: '))
    for i in range(num):
        n = int(input(f'Enter the {i+1}º value: '))
        tree.insert_level_order(n)
    print('Values inserted successfully into the tree!')
    
    print()
    level = int(input('Enter the level to show the nodes: '))
    print(f'The nodes at level {level} are:' ,end=' ')
    tree.nodes_at_level(level)
    print()

nodes_per_level()
