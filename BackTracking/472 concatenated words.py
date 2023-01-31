"""
https://leetcode.com/problems/concatenated-words/
"""


def findAllConcatenatedWordsInADict(words: list[str]) -> list[str]:
    wordSet = set(words)
    result = []

    def backtrack(pos, word):
        if pos == len(word):
            result.append(word)
            return True
        for end in range(pos + 1, len(word) + 1):
            if word[pos:end] in wordSet and (end - pos) != len(word):
                if backtrack(end, word):
                    return True
        return False

    for w in words:
        backtrack(0, w)

    return result


print(
    findAllConcatenatedWordsInADict(
        [
            "cat",
            "cats",
            "catsdogcats",
            "dog",
            "dogcatsdog",
            "hippopotamuses",
            "rat",
            "ratcatdogcat"
        ]
    )
)
