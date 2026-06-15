class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res = 0
        biggestEnd = intervals[0][1]
        for i in range(len(intervals)- 1):
            if biggestEnd > intervals[i + 1][0]:
                res += 1
            else:
                biggestEnd = intervals[i + 1][1]
        return res
