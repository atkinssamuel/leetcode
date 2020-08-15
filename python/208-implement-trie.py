# First pass hash-map solution: 42.4%, 220ms
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.starts_with_set = set()
        self.trie = set()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        starts_with_string = ""
        for char in word:
            starts_with_string += char
            self.starts_with_set.add(starts_with_string)
        self.trie.add(word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word in self.trie:
            return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if prefix in self.starts_with_set:
            return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)