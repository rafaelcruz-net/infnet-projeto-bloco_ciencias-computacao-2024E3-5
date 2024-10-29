class MinHeap:
    def __init__(self):
        #Lista que será usada para armazenar os elementos do heap
        self.heap = []
    
    def parent(self, index):
        # Retorna o indice pai de um nó atual
        return (index - 1) // 2
    
    def left(self, index):
        # Retorna o indice do filho a esquerda
        return 2 * index + 1
    
    def right(self, index):
        # Retorna o indice do filho a direita
        return 2 * (index + 1)
    
    def insert(self, element):
        #Adiciona o novo elemento ao final da heap
        self.heap.append(element)

        #Realiza a subida do elemento para manter a propriedade do heap
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        #Move o elemento para cima ate que a propriedade do heap seja mantida

        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            #Troca o elemento com o seu pai
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_min(self):
        if not self.heap:
            return None
        
        # Toma o menor elemento (a raiz) e subtitui pelo ultimo elemento
        root = self.heap[0]
        self.heap[0] = self.heap.pop()

        # Realiza a descida do elemento para manter a propriedade da heap
        self._heapify_down(0)

        return root

    def _heapify_down(self, index):
        #Move o elemento para baixo até que a propriedade da heap se mantida
        smallest = index

        left = self.left(index)
        right = self.right(index)

        if (left < len(self.heap) and self.heap[left] < self.heap[smallest]):
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            # Troca o elemento com o menor de seus filhos
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
    
    def get_min(self):

        #Retorna o menor elemento sem removê-lo
        if (self.heap):
            return self.heap[0]
        
        return None
    
    def size(self):
        #Retorna o tamanho da heap
        return len(self.heap)
    

if (__name__ == "__main__"):
    heap = MinHeap()
    heap.insert(10)
    heap.insert(20)
    heap.insert(5)
    heap.insert(1)
    heap.insert(25)
    

    print(heap.get_min()) # Saida deve ser 5

    print(heap.extract_min()) # Saida deve ser 5

    print(heap.get_min()) # Saida deve ser 10
        