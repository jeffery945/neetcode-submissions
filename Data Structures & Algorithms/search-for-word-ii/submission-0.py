class Node:
    def __init__(self):
        self.child = {}
        self.end = False
    def addWords(self, word):
        curr = self
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
        curr.end = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # backtracking + trie
        self.root = Node()
        for w in words:
            self.root.addWords(w)

        ROW, COL = len(board), len(board[0])
        res = set()
        visited = set()

        def dfs(r, c, node, word):
        
            if (r < 0 or c < 0 or r >= ROW or c >= COL or (r, c) in visited or board[r][c] not in node.child):
                return


            visited.add((r, c))
            node = node.child[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))

        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, self.root, "")

        return list(res)

