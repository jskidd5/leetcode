import functools


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # tmp = []
        # for i in intervals:
        #     tmp.append(Interval(i[0], i[1]))
        # intervals = tmp
        len_i = len(intervals)
        if len_i == 0:
            return intervals
        res = []
        intervals = sorted(intervals, key=(lambda x: x.start))
        tmp = intervals[0]
        for i in range(1, len_i):
            if intervals[i].start <= tmp.end:
                intervals[i].start = tmp.start
                if intervals[i].end <= tmp.end:
                    intervals[i].end = tmp.end
            else:
                res.append(tmp)
            tmp = intervals[i]
        res.append(tmp)
        # for i in res:
        #     print('%d    %d' % (i.start, i.end))
        return res


s = Solution()
print(s.merge([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]))
