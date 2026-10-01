class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        visited = [False] * n
        res = 0
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(node):
            visited[node] = True
            for a in adj[node]:
                if not visited[a]:
                    dfs(a)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1

        return res

            
