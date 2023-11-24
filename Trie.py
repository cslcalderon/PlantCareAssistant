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

    def insert_with_reversed_words(self, name):
        reversed_name = ' '.join(name.split()[::-1])  # Reverse the order of words
        node = self.root
        for char in reversed_name:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_words_from_node(node, prefix)

    def _get_words_from_node(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, next_node in node.children.items():
            words.extend(self._get_words_from_node(next_node, prefix + char))
        return words


def build_plant_trie(plant_names):
    trie = Trie()
    for name in plant_names:
        trie.insert_with_reversed_words(name.lower())
    return trie





