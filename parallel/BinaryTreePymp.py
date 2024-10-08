import pymp

class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)
    
    def insert(self, data): 
        #Insere dados na arvore de forma simples
        self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if (data < node.data):
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if (node.right is None):
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)
    
    def display(self, node):
        if (node):
            self.display(node.left)
            print(node.data, end=' ')
            self.display(node.right)
    
    def parallel_depth_traversal(self, node):
        if (node is None):
            return
        
        #imprimir o valor do nó
        print(node.data, end=' ')


        #Usar pymp para paralelizar a travessia dos filhos
        with pymp.Parallel(2) as p:
            if node.left:
                p.task = p.thread_num
                self.parallel_depth_traversal(node.left)
            if node.right:
                p.task = p.thread_num
                self.parallel_depth_traversal(node.right)




if (__name__ == "__main__"):
    tree = BinaryTree(4)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(6)
    tree.insert(5)
    tree.insert(7)

    print("Arvore binária em ordem (travessia por profundidade):")
    tree.display(tree.root)

    print()
    print("Travessia em profundidade de árvore (paralela):")
    tree.parallel_depth_traversal(tree.root)
    print()

        

    
        