class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def insert(self, word: str) -> None:
        tnode = self
        for ch in word:
            if ch not in tnode.children:
                tnode.children[ch] = Trie()
            tnode = tnode.children[ch]
        
        tnode.is_end = True
    
    def search(self, word: str) -> bool:
        def dfs(idx, node, diff) -> bool:
            if idx == len(word):
                return diff == 1 and node.is_end
            if word[idx] in node.children and dfs(idx + 1, node.children[word[idx]], diff):
                return True
            return diff == 0 and any(dfs(idx + 1, node.children[ch], 1) for ch in node.children if ch != word[idx])
        
        return dfs(0, self, 0)

class MagicDictionary:

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.trie.search(searchWord)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)