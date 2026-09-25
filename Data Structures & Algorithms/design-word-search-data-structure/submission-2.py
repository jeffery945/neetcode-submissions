class Node:
    def __init__(self):
        self.child = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
        curr.end = True
    def search(self, word: str) -> bool:

        def dfs(i, curr):
            for j in range(i, len(word)):
                if word[j] != '.':
                    if word[j] not in curr.child:
                        return False
                    curr = curr.child[word[j]]
                else:
                    for c in curr.child.values():
                        if dfs(j + 1, c):
                            return True
                    return False
            return curr.end

        return dfs(0, self.root)