class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)] # Inicializa a tabela com lista vazia

    # Função de hashing (módulo do tamanho da tabela)
    def hash_function(self, key):
        return hash(key) % self.size
    
    # Função para inserir um item na tabela hash
    def insert(self, key, value):
        index = self.hash_function(key)

        #Verificar se a chave já existe e atualiza o valor
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        
        #Caso contrario, adiciona um novo par (chave, valor)
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        
        # Busca valor pela chave transformado pelo hash function
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        # Não encontrei, retorno vazio
        return None
    
    def remove(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True
        return False
    
    def display(self): 
        for i, pair in enumerate(self.table):
            print(f'Index {i}: {pair}')

hash_table = Hashtable(10)

#Inserindo os valores
hash_table.insert("nome", 'Jõao')
hash_table.insert("idade", 40)
hash_table.insert("cidade", 'Rio de janeiro')

#Obtendo os valores
print(hash_table.get('nome'))
print(hash_table.get('cidade'))


#Exibindo a tabela hash
hash_table.display()


# Removendo um valor
hash_table.remove('cidade')

#Verificando se existe a chave
print(hash_table.get('cidade'))
        