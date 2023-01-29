"""
https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
"""


def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    """
    一看就知道要用 并查集 。
    """

    # 首先构造并查集 equivalent ，equivalent["f"] 代表与 "f" 等价的字母（但未必是最小）。
    equivalent = {chr(i): chr(i) for i in range(97, 123)}

    def find(x: str) -> str:
        if equivalent[x] == x:
            return x
        else:
            return find(equivalent[x])

    def merge(i: str, j: str) -> None:
        find_i = find(i)
        find_j = find(j)
        if find_i == find_j:
            pass
        elif find_i < find_j:
            equivalent[find_j] = find_i
        else:
            # find_i > find_j
            equivalent[find_i] = find_j

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        else:
            merge(s1[i], s2[i])

    # print(equivalent)

    ans = ""
    for i in range(len(baseStr)):
        ans += find(baseStr[i])

    return ans


print(
    smallestEquivalentString(
        "dfeffdfafbbebbebacbbdfcfdbcacdcbeeffdfebbdebbdafff",
        "adcdfabadbeeafeabbadcefcaabdecabfecffbabbfcdfcaaae",
        "myickvflcpfyqievitqtwvfpsrxigauvlqdtqhpfugguwfcpqv"
    )
)
print(
    smallestEquivalentString(
        "parker",
        "morris",
        "parser"
    )
)
print(
    smallestEquivalentString(
        "hello",
        "world",
        "hold"
    )
)
print(
    smallestEquivalentString(
        "leetcode",
        "programs",
        "sourcecode"
    )
)
