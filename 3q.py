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

    def search(self, v):
        if self.root is None:
            return False
        else:
            return self._search(self.root, v)
    
    def _search(self, node, v):
        if node is None:
            return False
        if node.value == v:
            return True
        if self._search(node.left, v):
            return True
        if self._search(node.right, v):
            return True

def insert(arv):
    for i in range(7):
        n = int(input(f'digite {i+1}º numero: '))
        arv.insert_level_order(n)
    print('Numbers inserted in the tree: ')
    arv.show_pre_order()

def check_presence(arv):
    v = int(input('arvore: ' ))
    if arv.search(v):
        print('Números inseridos na árvore: ')
    else:
        print('Número não está presente na árvore!')
tree = BinaryTree()
insert(tree)
print()
check_presence(tree)





