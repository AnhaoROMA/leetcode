"""
https://leetcode.com/problems/snakes-and-ladders/
"""


def snakes_and_ladders(board):
    # pre-process
    m = len(board)
    n = len(board[0])
    end_pos = m * n
    labels = dict()
    count = 1
    direction = True
    for i in range(m-1, -1, -1):
        if direction is True:
            for j in range(n):
                labels[count] = board[i][j]
                count += 1
        else:
            for j in range(n-1, -1, -1):
                labels[count] = board[i][j]
                count += 1
        direction = not direction
    del m
    del n
    del direction
    del count
    del i
    del j

    bfs = list()
    visited = set()
    # initialization
    bfs.append(1)
    visited.add(1)
    # do BFS
    res = 0
    while bfs:
        size = len(bfs)
        for _ in range(size):
            curr_pos = bfs.pop(0)
            if curr_pos == end_pos:
                return res
            for next_pos in range(curr_pos+1, min(end_pos, curr_pos+6)+1):
                if next_pos in visited:
                    continue
                visited.add(next_pos)
                if labels[next_pos] > 0:
                    next_pos = labels[next_pos]
                    # 注意！
                    # “跳过来的”和“走过来的”是要区分的！
                    # 因为“跳过来的”是不能再跳了，而走过来的却可以在这里跳。
                bfs.append(next_pos)
        res += 1
    return -1


print(
    snakes_and_ladders(
        [
            [-1,-1,-1,46,47,-1,-1,-1],
            [51,-1,-1,63,-1,31,21,-1],
            [-1,-1,26,-1,-1,38,-1,-1],
            [-1,-1,11,-1,14,23,56,57],
            [11,-1,-1,-1,49,36,-1,48],
            [-1,-1,-1,33,56,-1,57,21],
            [-1,-1,-1,-1,-1,-1, 2,-1],
            [-1,-1,-1, 8, 3,-1, 6,56]
        ]
    )
)
print(
    snakes_and_ladders(
        [
            [-1,7,-1],
            [-1,6, 9],
            [-1,-1,2]
        ]
    )
)
print(
    snakes_and_ladders(
        [
            [-1,4,-1],
            [6, 2, 6],
            [-1,3,-1]
        ]
    )
)
print(
    snakes_and_ladders(
        [
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,35,-1,-1,13,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,15,-1,-1,-1,-1]
        ]
    )
)
print(
    snakes_and_ladders(
        [
            [-1,-1],
            [-1, 3]
        ]
    )
)
