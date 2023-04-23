class Trie:
    # Your Trie object will be instantiated and called as such:
    # obj = Trie()
    # obj.insert(word)
    # param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)

    def __init__(self):
        self.children = dict

    def insert(self, word: str) -> None:
        nowNode = self.children
        for c in word:
            if c not in nowNode:
                nowNode[c] = dict
            nowNode = nowNode[c]
        nowNode['#'] = '#'

    def search(self, word: str) -> bool:
        nowNode = self.children
        for c in word:
            if c not in nowNode:
                return False
            else:
                nowNode = nowNode[c]
        return '#' in nowNode

    def startsWith(self, prefix: str) -> bool:
        nowNode = self.children
        for c in prefix:
            if c not in nowNode:
                return False
            else:
                nowNode = nowNode[c]
        return True
