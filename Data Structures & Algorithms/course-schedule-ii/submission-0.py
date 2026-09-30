class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = {i: [] for i in range(numCourses)}
        cycle = set()
        visited = set()
        res = []
        for c, p in prerequisites:
            pre[c].append(p)
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for p in pre[course]:
                if not dfs(p):
                    return False
            cycle.remove(course)

            visited.add(course)
            res.append(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res