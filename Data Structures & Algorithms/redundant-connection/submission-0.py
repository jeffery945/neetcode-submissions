class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 這題就是把所有點分成誰跟誰一組，同組的人如果再被指派到同一組代表cycle，return 他
        parent = [i for i in range(len(edges) + 1)] # 紀錄這個node的parent是誰 ith -> parent
        size = [1] * (len(edges) + 1) # 紀錄這個組size多大，eg: size[3] == 5, means以3為組長的組有5個人

        def find(node): # 找到這個組的組長
            root = parent[node]
            while root != parent[root]: #代表這個parent不是組長，要繼續往上找，儘量省空間
                parent[root] = parent[parent[root]]
                root = parent[root]
            return root

        def union(node1, node2):
            root1, root2 = find(node1), find(node2)

            if root1 == root2: #代表他們兩個原本已經同組，再加edge是造成cycle
                return False
            if size[root1] > size[root2]: # root1的組比較大，root2合併進root1
                parent[root2] = root1
                size[root1] += size[root2]
            else:
                parent[root1] = root2
                size[root2] += size[root1]
            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
