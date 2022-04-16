"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

"""
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

"""
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


# solution 1: 自上而下的迭代（无存储）
def climbing_stairs(num_stairs):
    if num_stairs == 1:
        return 1
    elif num_stairs == 2:
        return 2
    else:
        return climbing_stairs(num_stairs-1) + climbing_stairs(num_stairs-2)


# solution 2: 自上而下的迭代（有存储）
results = {0: 0, 1: 1, 2: 2}


def climbing_ladders(num_stairs) -> int:
    if num_stairs in results:
        return results[num_stairs]
    else:
        results[num_stairs] = climbing_ladders(num_stairs-1) + climbing_ladders(num_stairs-2)
        print(results)
        return results[num_stairs]


# solution 3: 自下而上的循环（有存储）
hashmap = {0: 0, 1: 1, 2: 2}


def climbing_a_building(num_stairs) -> int:
    if num_stairs in hashmap:
        return hashmap[num_stairs]
    else:
        for i in range(3, num_stairs+1):
            hashmap[i] = hashmap[i-1] + hashmap[i-2]
        return hashmap[num_stairs]


num = 3
print(climbing_a_building(num))
