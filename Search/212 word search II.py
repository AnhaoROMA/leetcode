"""
https://leetcode.com/problems/word-search-ii/
"""


def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    """
    词典法、前缀树、Trie
    """
    # m = len(board)
    # n = len(board[0])
    # dictionary = dict()
    #
    # def fill_dictionary(x: int, y: int, visited: list, pointer: dict) -> None:
    #     """
    #     编写词典
    #     """
    #     if len(visited) > 10:
    #         return
    #     character = board[x][y]
    #     if character not in pointer:
    #         pointer[character] = dict()
    #     if x < m-1 and (x+1, y) not in visited:
    #         fill_dictionary(x+1, y, visited+[(x, y)], pointer[character])
    #     if x > 0 and (x-1, y) not in visited:
    #         fill_dictionary(x-1, y, visited+[(x, y)], pointer[character])
    #     if y < n-1 and (x, y+1) not in visited:
    #         fill_dictionary(x, y+1, visited+[(x, y)], pointer[character])
    #     if y > 0 and (x, y-1) not in visited:
    #         fill_dictionary(x, y-1, visited+[(x, y)], pointer[character])
    #
    # for i in range(m):
    #     for j in range(n):
    #         fill_dictionary(x=i, y=j, visited=[], pointer=dictionary)
    # # print(dictionary)
    #
    # def judge(word: str) -> bool:
    #     """
    #     查询词典
    #     """
    #     temp_pointer = dictionary
    #     for character in word:
    #         if character not in temp_pointer:
    #             return False
    #         else:
    #             temp_pointer = temp_pointer[character]
    #     return True
    #
    # ans = []
    # for example in words:
    #     if judge(example) is True:
    #         ans.append(example)
    # return ans

    """
    从答案出发、判断 board 中能否找到
    """
    m = len(board)
    n = len(board[0])
    to_search = dict()
    for word in words:
        temp_pointer = to_search
        for character in word:
            if character not in temp_pointer:
                temp_pointer[character] = dict()
            temp_pointer = temp_pointer[character]
        temp_pointer["#"] = dict()
    # print(to_search)
    ans = []

    def explore(x: int, y: int, visited: list, pointer: dict) -> None:
        if len(visited) > 10:
            return
        char = board[x][y]
        if char in pointer:
            if "#" in pointer[char]:
                ans.append("".join([board[p][q] for p, q in visited+[(x, y)]]))
                del pointer[char]["#"]
            if x > 0 and (x-1, y) not in visited:
                explore(x-1, y, visited+[(x, y)], pointer[char])
            if x < m-1 and (x+1, y) not in visited:
                explore(x+1, y, visited + [(x, y)], pointer[char])
            if y > 0 and (x, y-1) not in visited:
                explore(x, y-1, visited+[(x, y)], pointer[char])
            if y < n-1 and (x, y+1) not in visited:
                explore(x, y+1, visited + [(x, y)], pointer[char])

    for i in range(m):
        for j in range(n):
            explore(x=i, y=j, visited=[], pointer=to_search)

    return ans


print(
    findWords(
        [
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"]
        ],
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    )
)
print(
    findWords(
        [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
        ["oath","pea","eat","rain"]
    )
)
