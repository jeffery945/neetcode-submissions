"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timetable = defaultdict(int)
        for i in intervals:
            timetable[i.start] += 1
            timetable[i.end] -= 1

        res = 0
        curr = 0
        for i in sorted(timetable.keys()):
            curr += timetable[i]
            res = max(res, curr)

        return res