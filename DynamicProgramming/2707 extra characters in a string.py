"""
https://leetcode.com/problems/extra-characters-in-a-string/

You are given a 0-indexed string s and a dictionary of words dictionary.
You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary.
There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

Example 1:
Input:
    s = "leetscode",
    dictionary = ["leet","code","leetcode"]
Output:
    1
Explanation:
    We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8.
    There is only 1 unused character (at index 4), so we return 1.

Example 2:
Input:
    s = "sayhelloworld",
    dictionary = ["hello","world"]
Output:
    3
Explanation:
    We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12.
    The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters.
    Hence, we return 3.

Constraints:
    1 <= s.length <= 50
    1 <= dictionary.length <= 50
    1 <= dictionary[i].length <= 50
    dictionary[i] and s consists of only lowercase English letters
    dictionary contains distinct words
"""


def min_extra_char(s: str, dictionary: list[str]) -> int:
    #
    # 动态规划 + 记忆表
    #
    MIN_LEN = len(min(dictionary, key=len))
    dictionary = set(dictionary)
    memory_table = [[-1 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
    # memory_table[i][j] := min_extra_char(s[i:j])

    def helping_hand(i: int, j: int) -> int:
        if memory_table[i][j] < 0:
            # memory_table[i][j] == -1
            if s[i:j] in dictionary:
                memory_table[i][j] = 0
            elif j-i <= MIN_LEN:
                memory_table[i][j] = j-i
            else:
                ans = j-i
                for k in range(i+1, j):
                    # 分为 s[i:k] 与 s[k:j] 两部分
                    ans = min(ans, helping_hand(i,k)+helping_hand(k,j))
                memory_table[i][j] = ans
            return memory_table[i][j]
        else:
            return memory_table[i][j]

    helping_hand(0, len(s))
    return memory_table[0][len(s)]


print(
    min_extra_char(
        s="leetscode",
        dictionary=["leet","code","leetcode"]
    )
)
print(
    min_extra_char(
        s="sayhelloworld",
        dictionary=["hello","world"]
    )
)
