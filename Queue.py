class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self): 
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila está vazia")
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
# USANDO A FILA
fila = Queue()
fila.enqueue('C')
fila.enqueue('B')
fila.enqueue('A')


print(fila.dequeue()) #SAIDA: C
print(fila.dequeue()) #SAIDA: B
print(fila.dequeue()) #SAIDA: A

        