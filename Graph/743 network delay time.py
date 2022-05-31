"""
https://leetcode.com/problems/network-delay-time/

You are given a network of n nodes, labeled from 1 to n. You are also given times,
a list of travel times as directed edges times[i] = (ui, vi, wi),
where ui is the source node,
      vi is the target node,
  and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k.
Return the time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.
"""
inf = 101


def dijkstra(times, n, k):
    map = [[inf for _ in range(n)] for _ in range(n)]
    for element in times:
        map[element[0]-1][element[1]-1] = element[2]
    # print(map)
    distance = [inf for _ in range(n)]
    distance[k-1] = 0
    # print(distance)
    visited = list()
    visited.append(k)
    while len(visited) > 0:
        temp_val = visited[0]
        visited.pop(0)
        temp_tab = map[temp_val-1]
        for i in range(len(temp_tab)):
            if i != temp_val - 1 and temp_tab[i] < inf:
                if distance[temp_val-1] + temp_tab[i] < distance[i]:
                    distance[i] = distance[temp_val-1] + temp_tab[i]
                    visited.append(i+1)
    # print(distance)
    if max(distance) == inf:
        return -1
    else:
        return max(distance)


a1 = [
    [2, 1, 1],
    [2, 3, 6],
    [3, 4, 1],
    [1, 3, 1]
]
b1 = 4
c1 = 2

print(dijkstra(a1, b1, c1))
