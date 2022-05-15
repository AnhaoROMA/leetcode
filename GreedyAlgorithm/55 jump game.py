"""
https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
which makes it impossible to reach the last index.
"""
"""
贪心和DP的比较：
贪心算法和动态规划算法都是由局部最优导出全局最优，这里不得不比较下二者的区别。

贪心算法：
贪心算法（又称贪婪算法）是指，在对问题求解时，总是做出在当前看来最好的选择。
也就是说，不从整体最优上加以考虑，他所作出的是在某种意义上的局部最优解。
1.贪心算法中，作出的每步贪心决策都无法改变，因为贪心策略是由上一步的最优解推导下一步的最优解，而上一步之前的最优解则不作保留；
2.由（1）中的介绍，可以知道贪心法正确的条件是：每一步的最优解一定包含上一步的最优解。

动态规划算法：
1.全局最优解中一定包含某个局部最优解，但不一定包含前一个局部最优解，因此需要记录之前的所有最优解；
2.动态规划的关键是状态转移方程，即如何由以求出的局部最优解来推导全局最优解；
3.边界条件：即最简单的，可以直接得出的局部最优解。
"""
"""
这个题的tag是贪心，贪心策略是我们每次都选取最优的策略，然后前面已经选好了的就不用管了。

这个题的贪心方法是，我们使用一个变量reach保存当前能到达的最后位置索引，那么在每个位置的时候判断这个位置能不能到达，
即位置的索引大于了reach说明前面无论怎么走也走不到这个位置，就返回False好了。
如果这个位置可以到达，那么要维护一下这个reach，更新策略是当前位置索引+这个数字代表的能向右走多少步，
这个代表了到达当前位置的时候向右能到达的最远距离，在这个最远距离以内的任何位置都能到，因为每次跳的步数可以变小的。
那么进行了这么一次循环以后，每个位置都判断为能到达，所以结果返回True就好了。

时间复杂度是O(N)，空间复杂度是O(1)。
"""


def jump(nums: list[int]) -> bool:
    reach = 0
    for i in range(len(nums)):
        if i > reach:
            return False
        reach = max(reach, i + nums[i])
    return True


a = [2, 3, 1, 1, 4]
b = [3, 2, 1, 0, 4]
print(jump(b))
