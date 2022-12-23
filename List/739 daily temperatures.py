"""
https://leetcode.com/problems/daily-temperatures/description/
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    单调栈
    """
    ans = [0] * len(temperatures)
    monotonic_stack = []
    i = len(temperatures) - 1
    while i >= 0:
        """
        将单调栈中、此后的、温度低于当日的记录给删掉。
        """
        while monotonic_stack and monotonic_stack[-1][0] <= temperatures[i]:
            monotonic_stack.pop()
        """
        获取需等待的天数。
        """
        if not monotonic_stack:
            # ans[i] = 0
            pass
        else:
            ans[i] = monotonic_stack[-1][1] - i
        """
        将“当前的”温度加入单调栈。
        """
        monotonic_stack.append((temperatures[i], i))
        """
        循环体。
        """
        i -= 1
    return ans


example_1 = [73, 74, 75, 71, 69, 72, 76, 73]
example_2 = [30, 40, 50, 60]
example_3 = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
print(
    daily_temperatures(
        example_3
    )
)
