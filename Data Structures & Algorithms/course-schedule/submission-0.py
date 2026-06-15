class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        pre = {i: [] for i in range(numCourses)}
        # 用pre去找這個node的prerequisite
        for b, f in prerequisites:
            pre[b].append(f)

        def dfs(node):
            if node in visit:
                return False
            if pre[node] == []:
                return True
            visit.add(node)
            for adj in pre[node]:
                if not dfs(adj):
                    return False
            visit.remove(node)
            pre[node] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True