class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self.front is None and self.rear is None
    
    def enqueue(self, value):
        new_node = Node(value)
        if (self.rear is None):
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("A lista encadeada está vazia")
        value = self.front.value
        self.front = self.front.next

        if (self.front is None):
            self.rear = None
        self._size -= 1
        return value
    def size(self):
        return self._size
    
    def traverse(self):
        current = self.front
        while current:
            print("{0}->".format(current.value), end="")
            current = current.next


#UTILIZANDO A LISTA
fila = LinkedQueue()

fila.enqueue('A')
fila.enqueue('B')
fila.enqueue('C')
fila.enqueue('D')


print(fila.traverse())

print(fila.dequeue())
print(fila.dequeue())

print(fila.traverse())

print(fila.dequeue())
print(fila.size())
    