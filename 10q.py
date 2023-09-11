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

    def find_maximum(self):
        if self.root is None:
            return None
        else:
            return self._find_maximum(self.root)
        
    def _find_maximum(self, node):
        if node is None:
            return float('-inf')
        maximum = node.value
        left_max = self._find_maximum(node.left)
        right_max = self._find_maximum(node.right)
        if left_max > maximum:
            maximum = left_max
        if right_max > maximum:
            maximum = right_max
        return maximum

def insert(arv):
    for i in range(7):
        n = int(input(f'Enter the {i+1}º number: '))
        arv.insert_level_order(n)
    print('Numbers inserted in the tree: ')
    arv.show_pre_order()

tree = BinaryTree()
insert(tree)
print()
maximum = tree.find_maximum()
print(f'The maximum value in this tree is: {maximum}')
