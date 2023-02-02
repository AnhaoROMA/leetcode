"""
https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals where intervals[i] = [start_i, end_i],
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
    1 <= intervals.length <= 10^5
    intervals[i].length == 2
    -5 * 10^4 <= start_i < end_i <= 5 * 10^4
"""


def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    """
    Greedy Algorithm
    A classic greedy case: interval scheduling problem.

    The heuristic is: always pick the interval with the earliest end time.
    Then you can get the maximal number of non-overlapping intervals (minimal number to remove).

    This is because,
    the interval with the earliest end time produces the maximal capacity to hold rest intervals.
    E.g.
        Suppose current earliest end time of the rest intervals is x.
        Then available time slot left for other intervals is [x:].
        But if we choose another interval with end time y,
        then available time slot would be [y:].
        Since x ≤ y, there is no way [y:] can hold more intervals then [x:].
        Thus, the heuristic holds.

    Therefore, we can sort interval by ending time and key track of current earliest end time.
    Once next interval's start time is earlier than current end time,
    then we have to remove one interval.
    Otherwise, we update earliest end time.
    """
    end, cnt = float('-inf'), 0
    for s, e in sorted(intervals, key=lambda x: x[1]):
        if s >= end:
            end = e
        else:
            cnt += 1
    return cnt
