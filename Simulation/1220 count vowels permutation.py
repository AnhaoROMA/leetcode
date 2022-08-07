"""
https://leetcode.com/problems/count-vowels-permutation/

Given an integer n,
your task is to count how many strings of length n can be formed under the following rules:
    Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
    Each vowel 'a' may only be followed by an 'e'.
    Each vowel 'e' may only be followed by an 'a' or an 'i'.
    Each vowel 'i' may not be followed by another 'i'.
    Each vowel 'o' may only be followed by an 'i' or a 'u'.
    Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9+7.
"""


def permutations(n: int) -> int:
    #
    # 以下是常规思路，毫无疑问的 TLE 了。
    #
    # rules = {
    #     "a": ["e"],
    #     "e": ["a", "i"],
    #     "i": ["a", "e", "o", "u"],
    #     "o": ["i", "u"],
    #     "u": ["a"]
    # }
    #
    # def f(last_char: str, left_num: int) -> int:
    #     if left_num == 0:
    #         return 1
    #     ans = 0
    #     for next_char in rules[last_char]:
    #         ans += f(next_char, left_num-1)
    #     return ans
    #
    # res = f("a", n-1) + f("e", n-1) + f("i", n-1) + f("o", n-1) + f("u", n-1)
    # return res % (10**9+7)

    """
    我们可以将这道题想象成一个树结构，树的分支数即是答案。

    比如当树的高度为1时，有5个分支，分别为a，e，i，o，u。

    当高度为2时：
    a下面有1个分支e
    e下面有2个分支a和i
    i下面有4个分支a，e，o，u
    o下面有2个分支i，u
    u下面有1个分支a
    一共是10个分支，分别为3个a，2个e，2个i，1个0，2个u。

    当高度为3时，与高度2时的处理类似：
    a下面有1个分支e，此时有3个a因此有3个分支e
    e下面有2个分支a和i，此时有2个e，因此分别有2个分支a和i
    i下面有4个分支a，e，o，u，此时有2个i，因此分别有2个分支a，e，o，u
    o下面有2个分支i和u，此时有1个o，因此有1个分支i和1个分支u
    u下面有1个分支a，此时有2个u，因此有2个分支a
    一共是19个分支。

    这就是基本的编程思路：
    首先我们先统计当前层分别有多少个a，e，i，o，u。
    它们的总和即是当层的结果。
    然后到下一层，分别看它们能出现多少分支，再统计出各个字母的个数。
    以此类推，直到循环至第n层结束。
    """
    rules = {
        "a": ["e"],
        "e": ["a", "i"],
        "i": ["a", "e", "o", "u"],
        "o": ["i", "u"],
        "u": ["a"]
    }
    level = 1
    cur_count = {
        "a": 1,
        "e": 1,
        "i": 1,
        "o": 1,
        "u": 1
    }
    while level < n:
        next_count = {
            "a": 0,
            "e": 0,
            "i": 0,
            "o": 0,
            "u": 0
        }
        for i in cur_count:
            for j in rules[i]:
                # print(i + "->" +j)
                next_count[j] += cur_count[i]
        cur_count = next_count
        level += 1
    return sum(list(cur_count.values()))


print(permutations(5))
