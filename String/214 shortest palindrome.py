"""
https://leetcode.com/problems/shortest-palindrome/

You are given a string s.
You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

Input: s = "aacecaaa"
Output: "aaacecaaa"

Input: s = "abcd"
Output: "dcbabcd"
"""


# 点拨：“寻找开头开始的最长回文串”

# 暴力解法：
# 先判断整个字符串是不是回文串，如果是的话，就直接将当前字符串返回。
# 不是的话，进行下一步。
# 判断去掉末尾 1 个字符的字符串是不是回文串，如果是的话，就将末尾的 1 个字符加到原字符串的头部返回。
# 不是的话，进行下一步。
# 判断去掉末尾 2 个字符的字符串是不是回文串，如果是的话，就将末尾的 2 个字符倒置后加到原字符串的头部返回。
# 不是的话，进行下一步。
# 判断去掉末尾 3 个字符的字符串是不是回文串，如果是的话，就将末尾的 3 个字符倒置后加到原字符串的头部返回。
# 不是的话，进行下一步。
# 。。。。。。
# 直到判断去掉末尾的 n-1 个字符，整个字符串剩下一个字符，把末尾的 n-1 个字符倒置后加到原字符串的头部返回。


# Manacher 算法
# https://zhuanlan.zhihu.com/p/70532099
def pre_process(s: str) -> str:
    """
        manacher算法的预处理部分
    """
    res = ""
    res += "^"
    for c in s:
        res += "#"
        res += c
    res += "#"
    res += "$"
    return res


def main(string: str) -> str:
    # 预处理
    s = pre_process(string)
    length = len(s)
    p = [0 for _ in range(length)]
    c = 0
    r = 0
    for i in range(1, length-1):
        i_mirror = 2 * c - i
        if r > i:
            p[i] = min(r-i, p[i_mirror])
        else:
            p[i] = 0
        while s[i+1+p[i]] == s[i-1-p[i]]:
            p[i] += 1
        if i+p[i] > r:
            c = i
            r = i + p[i]

    max_length = 0
    for i in range(1, length-1):
        # 我们要判断当前回文串是不是开头是不是从 0 开始的
        start = (i - p[i]) // 2
        if start == 0:
            if p[i] > max_length:
                max_length = p[i]
    return string[:max_length-1:-1] + string


print(main("abcd"))
print(main("aacecaaa"))
