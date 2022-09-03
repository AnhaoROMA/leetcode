"""
https://leetcode.com/problems/poor-pigs/
"""

import math

"""
举例说明。

假设: 总时间 minutesToTest = 60，死亡时间 minutesToDie = 15。

如果当前有 1 只小猪，最多可以喝 times = minutesToTest // minutesToDie = 4 次水。
最多可以喝 4 次水，能够携带 base = times + 1 = 5 个的信息量，也就是（为便于理解从 0 开始）：
(1) 喝 0 号死去 -> 0 号桶水有毒；
(2) 喝 1 号死去 -> 1 号桶水有毒；
(3) 喝 2 号死去 -> 2 号桶水有毒；
(4) 喝 3 号死去 -> 3 号桶水有毒；
(5) 喝了上述所有水依然活蹦乱跳 -> 4 号桶水有毒。
结论是 1 只小猪最多能够验证 5 桶水中哪只水桶含有毒药。

那么 2 只小猪可以验证的范围最多到多少呢？
结论是 25 桶水。
怎么做到呢？这也是最难的地方。关键在于，题目并没有说不可以喝混合液！

00 01 02 03 | 04
05 06 07 08 | 09
10 11 12 13 | 14
15 16 17 18 | 19
—— —— —— —— | ——
20 21 22 23 | 24

以上图为例，如果第 16 桶水是有毒的，那么其中一只小猪在第 2 次死去，另一只在第 4 次死去。
"""


def poor_pigs(buckets: int, minutes_to_die: int, minutes_to_test: int) -> int:
    times = minutes_to_test // minutes_to_die
    base = times + 1
    return ceil(math.log(buckets, base))
