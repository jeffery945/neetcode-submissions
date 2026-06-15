class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # cycle detection
        if n < len(edges) - 1:
            return False
        visit = set()
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n
            

