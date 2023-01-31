"""
https://leetcode.com/problems/remove-invalid-parentheses/

Given a string s that contains parentheses and letters,
remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals.
You may return the answer in any order.

Input: s = "()())()"
Output: ["(())()","()()()"]

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Input: s = ")("
Output: [""]

Constraints:
    1 <= s.length <= 25
    s consists of lowercase English letters and parentheses '(' and ')'.
    There will be at most 20 parentheses in s.
"""


def removeInvalidParentheses(s: str) -> list[str]:
    while s.startswith(")"):
        s = s[1:]

    def isValid(string) -> bool:
        # helper function, to check if para:string is valid
        count = 0
        for character in string:
            if character == "(":
                count += 1
            if character == ")":
                if count == 0:
                    return False
                count -= 1
        if count == 0:
            return True
        else:
            return False

    ans = []

    visited = set()
    bfs = list()
    # initialization
    visited.add(s)
    bfs.append(s)

    have_found = False
    while bfs:
        size = len(bfs)
        for _ in range(size):
            tmp = bfs.pop(0)
            if isValid(tmp) is True:
                # found an answer, add it to ans[]
                ans.append(tmp)
                have_found = True

            if have_found is True:
                continue

            # generate all possible states
            for i in range(len(tmp)):
                # we only try to remove left or right parentheses (ignore lowercase letters)
                if tmp[i] not in {"(", ")"}:
                    continue
                temp = tmp[:i] + tmp[i+1:]
                if temp not in visited:
                    visited.add(temp)
                    bfs.append(temp)
    return ans


print(removeInvalidParentheses("(a)())()"))
print(removeInvalidParentheses(")("))
