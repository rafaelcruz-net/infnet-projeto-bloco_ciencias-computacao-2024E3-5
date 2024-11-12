class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words(node, prefix)
    
    def _find_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, next_node in node.children.items():
            words.extend(self._find_words(next_node, prefix + char))
        
        return words

    def search_pattern(self, pattern):
        results = []
        self.pattern_search(self.root, pattern, results, "")
        return results
    
    def pattern_search(self, node, pattern, results, current_word):
        if (node.is_end_of_word and pattern in current_word):
            results.append(current_word)
        for char, child in node.children.items():
            self.pattern_search(child, pattern, results, current_word + char)
    
    def spell_checker(self, word):
        if (self.search(word)):
            return f"{word} está correto."
        else:
            suggestions = self.autocomplete(word[:2])
            return f"{word} não encontrada. Sugestões: [{suggestions}]" if suggestions else "Sem Sugestões"        

    

trie = Trie()
trie.insert("trip")
trie.insert("trap")
trie.insert("trick")
trie.insert("trie")
trie.insert("casa")
trie.insert("casinha")
trie.insert("casao")
trie.insert("cebola")
trie.insert("cebolinha")


#print(trie.autocomplete("ce"))

words = ["computer", "comutador", "compacto", "comunicação", "consulado", "campanha"]

for word in words:
    trie.insert(word)


words2 = ["cat", "dog", "carro", "bar", "cerveja"]
for word in words2:
    trie.insert(word)

print(trie.spell_checker("cerveja"))





        
        