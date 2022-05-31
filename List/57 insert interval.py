"""
https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals intervals
where intervals[i] = [starti, endi] represent the start and the end of the ith interval
and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end]
that represents the start and end of another interval.

Insert newInterval into intervals
such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals
(merge overlapping intervals if necessary).

Return intervals after the insertion.

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    for i in range(len(intervals)):
        if intervals[i][1] >= new_interval[0]:
            new_start = min(intervals[i][0], new_interval[0])
            for j in range(i, len(intervals)):
                if intervals[j][0] > new_interval[1]:
                    new_end = new_interval[1]
                    intervals[i:j] = [[new_start, new_end]]
                    return intervals
                elif intervals[j][0] <= new_interval[1] <= intervals[j][1]:
                    new_end = intervals[j][1]
                    intervals[i:j+1] = [[new_start, new_end]]
                    return intervals
                else:
                    # intervals[j][1] < new_interval[1]
                    continue
            new_end = new_interval[1]
            intervals[i:j+1] = [[new_start, new_end]]
            return intervals
    return intervals + [new_interval]


a = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
b = [4, 8]
c = [[1, 3], [6, 9]]
d = [2, 5]
e = [[1, 5]]
f = [2, 7]
g = [[1, 5]]
h = [0, 3]
print(insert_interval(g, h))
