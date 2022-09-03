"""
https://leetcode.com/problems/path-with-maximum-probability/
"""


# Wrong Answer!
def my_idea_1(n: int, edges: list[list[int]], weights: list[float], start: int, end: int) -> float:
    """
    我看到这一题的最初想法，是动态规划。
    按我的想法，设 f(c) := 从 c 到 end 的最大值；
              则 f(c) = max( f(i)*weight(c->i) )
    于是，我设置了 memory[] 这个记忆数组，用于存储 f(c) 的值。

    但是，结果是 Wrong Answer!

    为什么呢？
    我分析了一下，发现了问题所在。
    我希望 memory[i] 表示 “从 i 到 end 的最大值”，
    但是，在下面的代码里，memory[i] 表示 “去除了某些点后，从 i 到 end 的最大值”。
    去除了哪些点呢？
    在第一次计算 memory[i] 时，
    事实上，程序计算的是 “在去除了（当时的） visited[] 数组中的所有点后，从 i 到 end 的最大值”。
    之后，每次需要用到 memory[i] ，程序会“想当然地”直接返回，造成了错误。
    """
    connections = [{} for _ in range(n)]
    num_edges = len(edges)
    for i in range(num_edges):
        connections[edges[i][0]][edges[i][1]] = weights[i]
        connections[edges[i][1]][edges[i][0]] = weights[i]
    # print(connections)
    # memory[i]：从 i 到 end 的最大值 （注意，这里有问题！）
    memory = [-1 for _ in range(n)]
    memory[end] = 1

    def cal(c: int, v: list[int]) -> float:
        """
        c := cur_node, v := visited
        """
        if memory[c] > -1:
            pass
        else:
            temps = []
            for next_node in connections[c]:
                if next_node in v:
                    continue
                else:
                    tmp = connections[c][next_node] * cal(next_node, v + [c])
                    temps.append(tmp)
            if not temps:
                memory[c] = 0
            else:
                memory[c] = max(temps)
        return memory[c]

    return cal(c=start, v=[])


# TLE!
def my_idea_2(n: int, edges: list[list[int]], weights: list[float], start: int, end: int) -> float:
    """
    后来，我试了试 DFS ，果不其然，TLE 了。
    """
    connections = [{} for _ in range(n)]
    num_edges = len(edges)
    for i in range(num_edges):
        connections[edges[i][0]][edges[i][1]] = weights[i]
        connections[edges[i][1]][edges[i][0]] = weights[i]
    # print(connections)
    result = 0
    dfs = [
        [start, 1, []]
    ]
    while dfs:
        cur_node, temp_result, visited = dfs.pop()
        if cur_node == end:
            result = max(result, temp_result)
        else:
            for next_node in connections[cur_node]:
                if next_node in visited:
                    continue
                else:
                    dfs.append(
                        [
                            next_node, temp_result * connections[cur_node][next_node], visited + [cur_node]
                        ]
                    )
    return result


# TLE!
# 注：后来，勉强通过了。。。
def my_idea_3(n: int, edges: list[list[int]], weights: list[float], start: int, end: int) -> float:
    """
    后来，我想到了 Dijkstra 算法的思想：“这一次，仅仅考察上一次更新了的节点”。
    """
    connections = [{} for _ in range(n)]
    num_edges = len(edges)
    for i in range(num_edges):
        connections[edges[i][0]][edges[i][1]] = weights[i]
        connections[edges[i][1]][edges[i][0]] = weights[i]
    # print(connections)
    memory = [0 for _ in range(n)]
    memory[start] = 1
    affair_queue = [start]
    while affair_queue:
        tmp = affair_queue.pop(0)
        for next_node in connections[tmp]:
            if memory[tmp] * connections[tmp][next_node] > memory[next_node]:
                memory[next_node] = memory[tmp] * connections[tmp][next_node]
                if next_node not in affair_queue:
                    affair_queue.append(next_node)
    return memory[end]


def good_idea(n: int, edges: list[list[int]], weights: list[float], start: int, end: int) -> float:
    """
    沿用上面的思路（ Dijkstra 算法），但是巧用本题的 constraints ，
    不用等到穷尽（while affair_queue），提前结束。
    """
    connections = [{} for _ in range(n)]
    num_edges = len(edges)
    for i in range(num_edges):
        connections[edges[i][0]][edges[i][1]] = weights[i]
        connections[edges[i][1]][edges[i][0]] = weights[i]
    # print(connections)
    memory = [0 for _ in range(n)]
    memory[start] = 1
    affair_queue = [
        (1, start)
    ]
    while affair_queue:
        """
        这里，我们每次弹出 affair_queue 中 “最大的” 元素。
        注意，这里的 “最大” 是指 affair_queue[i][0] 最大（也就是“可以走的边里，值最大的”）。
        """
        where_to_pop = affair_queue.index(max(affair_queue))
        temp_value, cur_node = affair_queue.pop(where_to_pop)
        if cur_node == end:
            """
            这里妙就妙在，
            由于边的值不超过 1 ，所以边走得越少越好。
            故当“可以走的边里，值最大的边可以直通结束点”时，可以提前结束。
            """
            return temp_value
        for next_node in connections[cur_node]:
            tmp = temp_value*connections[cur_node][next_node]
            if tmp > memory[next_node]:
                memory[next_node] = tmp
                affair_queue.append((tmp, next_node))
    """
    显然，这里使用单调栈、在入栈的时候就排好序，会更好。
    """
    return memory[end]


print(my_idea_1(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
print(my_idea_1(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))
print(my_idea_1(3, [[0, 1]], [0.5], 0, 2))
print(my_idea_2(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
print(my_idea_2(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))
print(my_idea_2(3, [[0, 1]], [0.5], 0, 2))
print(my_idea_3(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
print(my_idea_3(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))
print(my_idea_3(3, [[0, 1]], [0.5], 0, 2))
print(good_idea(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
print(good_idea(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))
print(good_idea(3, [[0, 1]], [0.5], 0, 2))
