class Node:
    def __init__(self):
        self.map = {}
        self.flag = False


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        temp = self.head
        for c in word:
            if c not in temp.map:
                temp.map[c] = Node()
            temp = temp.map[c]
        temp.flag = True

    def search(self, word: str) -> bool:
        temp = self.head
        for c in word:
            if c not in temp.map:
                return False
            temp = temp.map[c]
        return temp.flag

    def startsWith(self, prefix: str) -> bool:
        temp = self.head
        for c in prefix:
            if c not in temp.map:
                return False
            temp = temp.map[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
