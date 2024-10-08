class Stack: 
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Não existem elementos na lista")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Não existem elementos na lista")
        return self.items[-1]
    
    def size(self):
        return len(self.items)

pilha = Stack()

pilha.push('A')
pilha.push('B')
pilha.push('C')

print(pilha.pop()) #SAIDA C

print(pilha.peek()) #SAIDA B
print(pilha.pop()) # SAIDA B

print(pilha.size()) # TAMANHO 1
print(pilha.pop()) # SAIDA A

print(pilha.pop()) # ERROR: NÃO EXISTEM ELEMENTOS


