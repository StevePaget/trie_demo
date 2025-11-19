f = open("sherlock.txt","r")

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert a word into the trie"""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
    
    def search(self, word):
        """Search for a word in the trie. Returns True if found, False otherwise"""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word
    
    def starts_with(self, prefix):
        """Check if there is any word in the trie that starts with the given prefix"""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

# Read words from sherlock.txt
words = []
alltext = f.readlines()
for line in alltext:
    line = line.strip().split()
    for word in line:
        words.append(word.lower())

# Build the trie with unique words
wordcount = 0
sherlockTrie = Trie()
unique_words = set()
for word in words:
    if word not in unique_words:
        sherlockTrie.insert(word)
        unique_words.add(word)
        wordcount += 1

print(f"{wordcount} unique words found")

# Interactive search
wordtoFind = ""
while wordtoFind != "quit":
    target = input("Enter a word to find (enter quit to exit): ")
    if target.lower() == "quit":
        break
    result = sherlockTrie.search(target.lower())
    if result:
        print(f"'{target}' found in the trie!")
    else:
        print(f"'{target}' not found in the trie.")
