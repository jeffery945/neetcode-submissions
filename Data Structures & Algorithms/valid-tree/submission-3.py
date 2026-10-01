class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        visited = set()
        if n < len(edges) - 1:
            return False

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for a in adj[node]:
                if a == parent:
                    continue
                if not dfs(a, node):
                    return False

            return True
        return dfs(0, -1) and len(visited) == n