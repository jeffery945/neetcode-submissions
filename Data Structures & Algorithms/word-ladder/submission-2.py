class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        nei = defaultdict(list)
        visited = set()
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                # pattern is like: hot-> *ot, h*t, ho*
                pattern = word[:i] + "*" + word[i + 1:]
                nei[pattern].append(word) 
        
        q = deque()
        q.append(beginWord)
        visited.add(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiword in nei[pattern]:
                        if neiword not in visited:
                            visited.add(neiword)
                            q.append(neiword)
            res += 1

        return 0