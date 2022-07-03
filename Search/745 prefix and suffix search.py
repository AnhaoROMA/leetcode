"""
https://leetcode.com/problems/prefix-and-suffix-search/

Design a special dictionary with some words
that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:
    WordFilter(string[] words) Initializes the object with the words in the dictionary.

    f(string prefix, string suffix) Returns the index of the word in the dictionary,
    which has the prefix prefix and the suffix suffix.
    If there is more than one valid index, return the largest of them.
    If there is no such word in the dictionary, return -1.

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]
"""


class WordFilter:

    def __init__(self, words: List[str]):
        self.library = dict()
        self.length = 0
        for word in words:
            k = len(word)
            i = 0
            while i < k + 1:
                j = 0
                while j < k + 1:
                    # print(
                    #     word[:i], word[j:]
                    # )
                    tmp = word[:i] + "-" + word[j:]
                    self.library[tmp] = self.length

                    j += 1
                i += 1
            self.length += 1

    def f(self, prefix: str, suffix: str) -> int:
        tmp = prefix + "-" + suffix
        if tmp in self.library:
            return self.library[tmp]
        return -1
