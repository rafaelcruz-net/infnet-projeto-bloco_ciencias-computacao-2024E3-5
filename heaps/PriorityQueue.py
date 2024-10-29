class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def parent(self, index):
        # Retorna o indice pai de um nó atual
        return (index - 1) // 2
    
    def left(self, index):
        # Retorna o indice do filho a esquerda
        return 2 * index + 1
    
    def right(self, index):
        # Retorna o indice do filho a direita
        return 2 * (index + 1)
    

    def insert(self, element, priority):
        
        #Adiciona o elemento com um tupla (prioridade e elemento)
        self.queue.append((priority, element))

        # Ajusta a posição para manter o max-heap
        self._heapify_up(len(self.queue) - 1)
    
    def _heapify_up(self, index):
        #Move o elemento para cima ate que a propriedade do heap seja mantida
        while index > 0 and self.queue[self.parent(index)][0] < self.queue[index][0]:
            #Troca o elemento com o seu pai
            self.queue[index], self.queue[self.parent(index)] = self.queue[self.parent(index)], self.queue[index]
            index = self.parent(index) 
    
    def extract_max(self):
        if not self.queue:
            return None
        
        # Toma o menor elemento (a raiz) e subtitui pelo ultimo elemento
        root = self.queue[0]
        self.queue[0] = self.queue.pop()

        # Realiza a descida do elemento para manter a propriedade da heap
        self._heapify_down(0)

        return root[1]
    
    def _heapify_down(self, index):
        #Move o elemento para baixo até que a propriedade da heap se mantida
        largest = index

        left = self.left(index)
        right = self.right(index)

        if  left < len(self.queue) and self.queue[left][0] > self.queue[largest][0]:
            largest = left
        if right < len(self.queue) and self.queue[right][0] > self.queue[largest][0]:
            largest = right

        if largest != index:
            # Troca o elemento com o menor de seus filhos
            self.queue[index], self.queue[largest] = self.queue[largest], self.queue[index]
            self._heapify_down(largest)

    def peek(self):
        if self.queue:
            return self.queue[0][1]
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
        

if (__name__ == "__main__"):
    pq = PriorityQueue()
    pq.insert("TASK A", priority=2)
    pq.insert("TASK B", priority=5)
    pq.insert("TASK C", priority=1)
    pq.insert("TASK D", priority=3)

    print(pq.peek()) #Saida: "TASK B"
    print(pq.extract_max()) #Saida: "TASK B"
    print(pq.peek()) #Saida: "TASK D"
    print(pq.size()) #SAIDA: 3
    print(pq.is_empty()) #SAIDA: FALSE
    print(pq.extract_max()) #Saida: "TASK D"
    print(pq.peek()) #Saida: "TASK A"
    print(pq.extract_max()) #Saida: "TASK A"
    print(pq.peek()) #Saida: "TASK C"
    print(pq.size()) #SAIDA: 1






        