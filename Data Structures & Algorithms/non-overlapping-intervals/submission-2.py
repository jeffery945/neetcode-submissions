class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res = 0
        largestend = intervals[0][1]
        for i in range(len(intervals) - 1):
            if largestend > intervals[i + 1][0]:
                res += 1
            else:
                largestend = intervals[i + 1][1]
        return res