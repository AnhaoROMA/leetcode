"""
https://leetcode.com/problems/longest-string-chain/
"""


#
# 首先来定义 dp 数组。
# 这里用一个一维的数组就行了，其中 dp[i] 表示 以第i个单词为结尾的链的最大长度。
#
# 下面来推导状态转移方程。
# 对于当前位置的单词，需要遍历前面所有的单词。
# （ 这里需要先给单词按长度排个序，因为只有长度小1的单词才有可能是前驱。 ）
# 若是前任关系，则取 dp[index] = max(dp[index], dp[j] + 1) 。
#
def judge(shorter: str, longer: str) -> bool:
    """
    判断 shorter 是否是 longer 的前驱。
    其中，longer 比 shorter 长 1 个字符。
    """
    length = len(longer)
    for i in range(length):
        modified = longer[:i] + longer[i+1:]
        if modified == shorter:
            return True
    return False


def longest(words: list[str]) -> int:
    length = len(words)
    if length == 1:
        return 1
    words.sort(key=lambda i: len(i))

    dp = [1 for _ in range(length)]
    index = 1
    while index < length:
        j = index - 1
        while j >= 0:
            if len(words[j]) + 1 < len(words[index]):
                break
            elif len(words[j]) + 1 == len(words[index]) and judge(words[j], words[index]):
                dp[index] = max(dp[index], dp[j] + 1)
                # 注意这里不能 break !
                # 因为要判断所有可能性。
                j -= 1
            else:
                j -= 1
        index += 1
    return max(dp)


print(longest(["a", "b", "ba", "bca", "bda", "bdca"]))
print(longest(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(longest(["bdca", "bda", "ca", "dca", "a"]))
print(longest(["a", "b", "ba", "bca", "bda", "bdca"]))
print(longest(["a", "b", "ab", "bac"]))
print(longest(["a", "ab", "ac", "bd", "abc", "abd", "abdd"]))