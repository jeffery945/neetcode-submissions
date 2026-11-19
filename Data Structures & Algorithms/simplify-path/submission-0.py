class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        new_path = path.split("/")

        for curr in new_path:
            if curr == "..":
                if stack:
                    stack.pop()
            elif curr != "" and curr != ".":
                stack.append(curr)
        
        return "/" + "/".join(stack)