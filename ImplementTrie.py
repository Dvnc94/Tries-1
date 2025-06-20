# Time Complexity : O(N)
# Space Complexity : O(N)

class TrieNode:
    def __init__(self):
        self.children={}
        self.IsEnd=False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if (i not in curr.children):
                curr.children[i]=TrieNode()    
            curr=curr.children[i]
        curr.IsEnd=True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if (i not in curr.children):
                return False
            curr=curr.children[i]
        return curr.IsEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if (i not in curr.children):
                return False
            curr=curr.children[i]
        return True