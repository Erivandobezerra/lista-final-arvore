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

    def show_in_order(self):
        if self.root is None:
            print("The root is empty.")
        else:
            self.show_in_order_recursive(self.root)
        
    def show_in_order_recursive(self, node):
        if node.left is not None:
            self.show_in_order_recursive(node.left)
        print(node.value, end=' ')
        if node.right is not None:
            self.show_in_order_recursive(node.right)
        
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

def insert(arv):
    for i in range(7):
        n = int(input(f'Enter the {i+1}º number: '))
        arv.insert_level_order(n)
    print('Numbers inserted in the tree: ')
    arv.show_in_order()

tree = BinaryTree()
insert(tree)
print()
height = tree.height()
print('Tree height: ', height)
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

    def show_in_order(self):
        if self.root is None:
            print("Está vazia.")
        else:
            self.show_in_order_recursive(self.root)
        
    def show_in_order_recursive(self, node):
        if node.left is not None:
            self.show_in_order_recursive(node.left)
        print(node.value, end=' ')
        if node.right is not None:
            self.show_in_order_recursive(node.right)
        
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

def insert(arv):
    for i in range(7):
        n = int(input(f'Digite {i+1}º numero: '))
        arv.insert_level_order(n)
    print('Numeros inseridos na arvore: ')
    arv.show_in_order()

tree = BinaryTree()
insert(tree)
print()
height = tree.height()
print('Tree height: ', height)
