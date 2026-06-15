class TreeNode:
    def __init__(self):
        self.child = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.child:
                curr.child[c] = TreeNode()
            curr = curr.child[c]
        curr.end = True
    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return True
        