# 208. 实现 Trie (前缀树)

# 插入一个单词（键、字符串）。时间：O(n)，空间：O(n)
# 查找一个单词（键、字符串）。时间：O(n)，空间：O(1)
# 查找单词（键、字符串）前缀。时间：O(m)，空间：O(1)

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for s in word:
            node = node.children[s]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for s in word:
            if s in node.children:
                node = node.children[s]
            else:
                return False
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for s in prefix:
            if s in node.children:
                node = node.children[s]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)










