"""
https://leetcode.com/problems/jump-game-iv/

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:
    i + 1 where: i + 1 < arr.length.
    i - 1 where: i - 1 >= 0.
    j where: arr[i] == arr[j] and i != j.

Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside the array at any time.

Constraints:
    1 <= arr.length <= 5 * 10^4
    -10^8 <= arr[i] <= 10^8
"""


def minJumps(arr: list[int]) -> int:
    length = len(arr)
    answer = [-1 for _ in range(length)]
    book = dict()
    for i in range(length):
        if arr[i] not in book:
            book[arr[i]] = set()
        book[arr[i]].add(i)
    bfs = set()
    bfs.add(length-1)
    answer[length-1] = 0
    while bfs:
        new_bfs = set()
        for i in bfs:
            if i-1 > -1 and answer[i-1] < 0:
                answer[i-1] = answer[i] + 1
                new_bfs.add(i-1)
            if i+1 < length and answer[i+1] < 0:
                answer[i+1] = answer[i] + 1
                new_bfs.add(i+1)
            for j in book[arr[i]]:
                if answer[j] < 0:
                    answer[j] = answer[i] + 1
                    new_bfs.add(j)
            book[arr[i]].clear()  # 很重要！避免重复访问。
        bfs = new_bfs
    # print(answer)
    return answer[0]


print(minJumps([100,-23,-23,404,100,23,23,23,3,404]))
print(minJumps([7]))
print(minJumps([7,6,9,6,9,6,9,7]))
