class TreeNode:
    def __init__(self):
        self.child = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TreeNode()
            curr = curr.child[c]
        curr.end = True


    def search(self, word: str) -> bool:
        def dfs(i, cur):
            # if we met ., just walk through all the child
            curr = cur
            for j in range(i, len(word)):
                c = word[j]
                if c != ".":
                    if c not in curr.child:
                        return False
                    curr = curr.child[c]
                else:
                    for c in curr.child.values():
                        if dfs(j + 1, c):
                            return True
                    return False
            return curr.end

        return dfs(0, self.root)
            
