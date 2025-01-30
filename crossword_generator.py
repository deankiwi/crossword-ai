class TrieNode:
    """A node in the Trie data structure"""

    def __init__(self, curr_letters):
        self.curr_letters = curr_letters
        self.children = {}
        self.is_end_of_word = False
        self.before = None


class Trie:
    """A Trie data structure"""

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        """Insert a word into the Trie"""
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(current_node.curr_letters + char)
                current_node.children[char].before = current_node

            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, prefix):
        """Search for words starting with a given prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        # If we reach this point, it means the prefix is in the Trie
        found_words = []

        def traverse(node, word):
            nonlocal found_words
            if node.is_end_of_word:
                found_words.append(prefix + word)
            for char, child_node in node.children.items():
                traverse(child_node, word + char)

        traverse(node, "")
        return found_words

    def getTree(this) -> TrieNode:
        return this.root


def load_and_build_trie(file_path) -> Trie:
    """Load words from a file and build the Trie"""
    trie = Trie()

    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            # Split each line into words
            words = line.split()
            for word in words:
                # Remove punctuation from the word
                word = "".join(e for e in word if e.isalnum())
                trie.insert(word)

    return trie


def load_and_build_trie_with_length(file_path: str, max_length: int) -> Trie:
    """Load words from a file and build the Trie"""
    trie = Trie()

    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            # Split each line into words
            words = line.split()
            for word in words:
                # Remove punctuation from the word
                word = "".join(e for e in word if e.isalnum())
                if len(word) == max_length:
                    trie.insert(word)

    return trie


# Example usage:
# trie = load_and_build_trie_with_length("popular_dictionary.txt", 6)

# print(trie.search("pre"))

# print(trie.getTree().children.items())


# for t in trie.getTree().children:
#     print(t)
def print_crossword_from_across_tree(words: list):
    words_copy = words[:]
    for i in range(len(words_copy)):
        while words_copy[i].before:
            words_copy[i] = words_copy[i].before
    for i in range(len(words_copy)):

        words_copy[i] = words_copy[i].before


def create_crossword(width, height):
    trie_w = load_and_build_trie_with_length("popular_dictionary.txt", width).getTree()
    if width == height:
        trie_h = trie_w
    else:
        trie_h = load_and_build_trie_with_length(
            "popular_dictionary.txt", height
        ).getTree()

    words_down = [trie_h for _ in range(width)]

    # first line across go through each word
    # second line go through each letter it can use and check if possible each time
    def helper(curr_word_across: TrieNode, across_i: int):
        if curr_word_across.is_end_of_word:
            if words_down[-1].is_end_of_word:
                print("WE FOUND AN ANSWER!!!")
                for word in words_down:
                    print(list(word.curr_letters))
                return
            helper(trie_w, 0)

        # TODO for loop through words_down as you'll only have the letters left

        for char in curr_word_across.children:
            if char in words_down[across_i].children:
                temp = words_down[across_i]
                words_down[across_i] = words_down[across_i].children[char]
                helper(curr_word_across.children[char], across_i + 1)
                words_down[across_i] = temp

    helper(trie_w, 0)


create_crossword(6, 6)
