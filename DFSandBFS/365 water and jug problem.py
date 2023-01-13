"""
https://leetcode.com/problems/water-and-jug-problem/
"""


def canMeasureWater(jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
    visited = set()
    bfs = list()
    bfs.append((0, 0))
    visited.add((0, 0))
    while bfs:
        water_1, water_2 = bfs.pop(0)
        if targetCapacity == water_1 or targetCapacity == water_2 or targetCapacity == water_1 + water_2:
            return True
        # 为水瓶加满水
        tmp = (jug1Capacity, water_2)
        if tmp not in visited:
            bfs.append(tmp)
            visited.add(tmp)
        tmp = (water_1, jug2Capacity)
        if tmp not in visited:
            bfs.append(tmp)
            visited.add(tmp)
        # 倒空水瓶
        tmp = (0, water_2)
        if tmp not in visited:
            bfs.append(tmp)
            visited.add(tmp)
        tmp = (water_1, 0)
        if tmp not in visited:
            bfs.append(tmp)
            visited.add(tmp)
        # 相互倾倒
        ## 水瓶 1 -> 水瓶 2
        quantity_to_pour = min(water_1, jug2Capacity - water_2)
        tmp = (water_1 - quantity_to_pour, water_2 + quantity_to_pour)
        if tmp not in visited:
            bfs.append(tmp)
            visited.add(tmp)
        ## 水瓶 2 -> 水瓶 1
        quantity_to_pour = min(water_2, jug1Capacity - water_1)
        tmp = (water_1 + quantity_to_pour, water_2 - quantity_to_pour)
        if tmp not in visited:
            bfs.append(tmp)
            visited.add(tmp)
    return False


print(canMeasureWater(3, 5, 4))
print(canMeasureWater(2, 6, 5))
print(canMeasureWater(1, 2, 3))
