class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i: [] for i in range(numCourses)}
        visited = set()

        for crs, pr in prerequisites:
            pre[crs].append(pr)

        def dfs(course):
            # in visited means we met it before, so it forms a loop
            if course in visited:
                return False
            if pre[course] == []:
                return True
            
            visited.add(course)
            # iterate every prerequisites in this course, to find if its prerequisites are gonna be ok
            for pr in pre[course]:
                if not dfs(pr):
                    return False

            visited.remove(course)
            pre[course] = [] # let next node do not have to iterate again
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True