"""
https://leetcode.com/problems/reconstruct-itinerary/

You are given a list of airline tickets where tickets[i] = [from_i, to_i]
    represent the departure and the arrival airports of one flight.
Reconstruct the itinerary in order and return it.

All tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
If there are multiple valid itineraries,
    you should return the itinerary that has the smallest lexical order when read as a single string.
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

You may assume all tickets form at least one valid itinerary.
You must use all the tickets once and only once.

Input:
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output:
    ["JFK","MUC","LHR","SFO","SJC"]

Input:
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output:
    ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation:
    Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints:
    1 <= tickets.length <= 300
    tickets[i].length == 2
    from_i.length == 3
    to_i.length == 3
    from_i and to_i consist of uppercase English letters.
    from_i != to_i
"""


def findItinerary(tickets: list[list[str]]) -> list[str]:
    """
    出度 与 入度 、一笔画问题

    the fact 在一张图中，若存在度为奇数的节点，则这样的节点必是两个，且一个是起点与终点，
                       若不存在度为奇数的节点，则任意一个节点都可以作为起点、同时也是终点。
    （而本题要求 JFK 一定是起点。）

    当然本题可以直接用 DFS 或者 回溯法 求解。
    """
    graph = {}
    for f, t in tickets:
        if f not in graph:
            graph[f] = {}
        if t not in graph[f]:
            graph[f][t] = 0
        graph[f][t] += 1
    # print(graph)
    length = len(tickets)  # “旅行”的次数
    all_possible_paths = []

    #
    # TLE!
    #
    # def back_tracing(cur_pos: str, left_steps: int, already_travelled: list[str]):
    #     if left_steps == 0:
    #         all_possible_paths.append(already_travelled)
    #     else:
    #         if cur_pos in graph:
    #             for next_pos in graph[cur_pos]:
    #                 if graph[cur_pos][next_pos] == 0:
    #                     continue
    #                 else:
    #                     graph[cur_pos][next_pos] -= 1
    #                     back_tracing(next_pos, left_steps-1, already_travelled+[next_pos])
    #                     graph[cur_pos][next_pos] += 1  # 回溯
    #

    def back_tracing(cur_pos: str, left_steps: int, already_travelled: list[str]) -> bool:
        """想办法提早发现，即 early exit """
        if left_steps == 0:
            all_possible_paths.append(already_travelled)
            return True
        else:
            if cur_pos in graph:
                candidates = []
                for next_pos in graph[cur_pos]:
                    if graph[cur_pos][next_pos] > 0:
                        candidates.append(next_pos)
                candidates.sort()  # 想办法提早发现
                for next_pos in candidates:
                    graph[cur_pos][next_pos] -= 1
                    if back_tracing(next_pos, left_steps-1, already_travelled+[next_pos]) is True:
                        return True
                    else:
                        graph[cur_pos][next_pos] += 1  # 回溯
                return False
            else:
                # cur_pos not in graph
                return False

    back_tracing(cur_pos="JFK", left_steps=length, already_travelled=["JFK"])

    # print(all_possible_paths)
    return min(all_possible_paths)


print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))