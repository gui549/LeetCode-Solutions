class Trie:

    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        current_node = self.root
        for i in range(len(word)):
            if word[i] not in current_node:
                current_node[word[i]] = dict()
            
            current_node = current_node[word[i]]
        current_node["END"] = word

    def search(self, word: str) -> bool:
        current_node = self.root
        for i in range (len(word)):
            if word[i] not in current_node:
                return False

            current_node = current_node[word[i]]
            
        return "END" in current_node

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for i in range (len(prefix)):
            if prefix[i] not in current_node:
                return False

            current_node = current_node[prefix[i]]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)