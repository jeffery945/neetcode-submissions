class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        q = deque()
        time = 0
        # maxheap records how many times this charactor needs to be processed
        # q records [how many times this charactor needs to be processed, the time it can be processed]
        while maxheap or q:
            time += 1
            if not maxheap: # if all the tasks are in cooldown, go directly to time that the first task in queue cooldown
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxheap) # it is -1, but maxheap is negative, so +1
                if cnt: # if cnt is 0, it means that it done. If it is not, push[how many times it left, the time it finish cooldown]
                    q.append([cnt, time + n])

            
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])

                
        return time