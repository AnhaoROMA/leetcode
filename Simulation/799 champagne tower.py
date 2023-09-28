"""
https://leetcode.com/problems/champagne-tower
"""


def champagne_tower(poured: int, query_row: int, query_glass: int) -> float:
    tower = [[0.0 for _ in range(i+1)] for i in range(query_row+2)]
    tower[0][0] = float(poured)
    for i in range(query_row+1):
        for j in range(i+1):
            if tower[i][j] > 1.0:
                tmp = (tower[i][j] - 1) / 2
                tower[i][j] = 1.0
                tower[i+1][j] += tmp
                tower[i+1][j+1] += tmp
    # print(tower)
    return tower[query_row][query_glass]


print(champagne_tower(2, 1, 1))
print(champagne_tower(100000009, 33, 17))
