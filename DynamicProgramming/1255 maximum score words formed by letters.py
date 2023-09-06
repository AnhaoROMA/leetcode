"""
https://leetcode.com/problems/maximum-score-words-formed-by-letters/

Given a list of words, list of single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words
    formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once.

Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

Constraints:
    1 <= words.length <= 14
    1 <= words[i].length <= 15
    1 <= letters.length <= 100
    letters[i].length == 1
    score.length == 26
    0 <= score[i] <= 10
    words[i], letters[i] contains only lower case English letters.
"""

from collections import Counter


def maxScoreWords(words: list[str], letters: list[str], score: list[int]):

    weights = dict()
    for i in range(26):
        weights[chr(97+i)] = score[i]
    values = dict()
    for word in words:
        value = 0
        for character in word:
            value += weights[character]
        values[word] = value
    del word
    del value
    del character
    del weights

    length = len(words)

    def dfs(left_source: dict, current_index: int) -> int:
        if current_index == length:
            return 0
        word = Counter(words[current_index])
        for character in word:
            if character not in left_source or left_source[character] < word[character]:
                return dfs(left_source, current_index+1)
        next_source = {
            character: left_source[character]-word[character]
            for character in left_source
        }
        return max(
            dfs(left_source, current_index+1),
            values[words[current_index]]+dfs(next_source, current_index+1)
        )

    return dfs(left_source=Counter(letters), current_index=0)


print(
    maxScoreWords(
        ["dog","cat","dad","good"],
        ["a","a","c","d","d","d","g","o","o"],
        [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    )
)
print(
    maxScoreWords(
        ["xxxz","ax","bx","cx"],
        ["z","a","b","c","x","x","x"],
        [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
    )
)
print(
    maxScoreWords(
        ["leetcode"],
        ["l","e","t","c","o","d"],
        [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
    )
)
