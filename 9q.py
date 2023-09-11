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

    def count_nodes(self):
        if self.root is None:
            return 0
        else:
            return self._count_nodes(self.root)
        
    def _count_nodes(self, node):
        if node is None:
            return 0
        count = 1
        if node.left is not None:
            count += self._count_nodes(node.left)
        if node.right is not None:
            count += self._count_nodes(node.right)
        return count

num = int(input('How many nodes do you want to add to the tree?: '))   
def insert(arv):
    for i in range(num):
        n = int(input(f'Enter the {i+1}º number: '))
        arv.insert_level_order(n)
    print('Numbers inserted in the tree: ')
    arv.show_pre_order()

tree = BinaryTree()
insert(tree)
print()
node_count = tree.count_nodes()
print(f'The tree has: {node_count} nodes')
