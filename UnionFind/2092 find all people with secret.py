"""
https://leetcode.com/problems/find-all-people-with-secret/
"""

from collections import defaultdict


def findAllPeople(n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
    timeslots = defaultdict(list)
    for i, j, time in meetings:
        timeslots[time].append((i, j))

    def grouping(paths):
        parent = dict()
        rank = dict()
        for x, y in paths:
            if x not in parent:
                parent[x] = x
            if x not in rank:
                rank[x] = 0
            if y not in parent:
                parent[y] = y
            if y not in rank:
                rank[y] = 0
            x_root = x
            while parent[x_root] != x_root:
                x_root = parent[x_root]
            y_root = y
            while parent[y_root] != y_root:
                y_root = parent[y_root]
            if x_root != y_root:
                if rank[x_root] > rank[y_root]:
                    parent[y_root] = x_root
                elif rank[x_root] < rank[y_root]:
                    parent[x_root] = y_root
                else:
                    parent[x_root] = y_root
                    rank[y_root] += 1
        groups = defaultdict(list)
        for k in parent.keys():
            k_root = k
            while parent[k_root] != k_root:
                k_root = parent[k_root]
            parent[k] = k_root
            groups[parent[k]].append(k)
        ans = list()
        for k in groups:
            ans.append(set(groups[k]))
        return ans

    for time in timeslots:
        timeslots[time] = grouping(timeslots[time])

    already_know = set()
    already_know.add(0)
    already_know.add(firstPerson)
    for time in sorted(timeslots.keys()):
        for parts in timeslots[time]:
            if already_know & parts:
                already_know |= parts

    return list(already_know)
