class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, node):
        if (data < node.data):
            if (node.left is None):
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if (node.right is None):
                node.right = Node(data)
            else:
                self._insert(data, node.right)
                
    def inorder(self, node):
        if (node is not None):
            self.inorder(node.left)
            print(node.data, end = " ")
            self.inorder(node.right)
    
bt = BinaryTree()

bt.insert(10)
bt.insert(5)
bt.insert(20)
bt.insert(3)
bt.insert(7)

bt.inorder(bt.root)

        