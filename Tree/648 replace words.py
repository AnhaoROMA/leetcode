"""
https://leetcode.com/problems/replace-words/

In English, we have a concept called root,
which can be followed by some other word to form another longer word - let's call this word successor.
For example,
    when the root "an" is followed by the successor word "other",
    we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces,
replace all the successors in the sentence with the root forming it.
If a successor can be replaced by more than one root,
replace it with the root that has the shortest length.

Return the sentence after the replacement.
"""


def replaceWords(dictionary: list[str], sentence: str) -> str:
    """
        前缀树
    """
    trie = dict()
    for word in dictionary:
        temp_pointer = trie
        for character in word:
            if character not in temp_pointer:
                temp_pointer[character] = dict()
            temp_pointer = temp_pointer[character]
        temp_pointer["*"] = True
    # print(trie)

    words = sentence.split()
    for i in range(len(words)):
        word = words[i]
        temp_pointer = trie
        for j in range(len(word)):
            if "*" in temp_pointer:
                words[i] = word[:j]
                break
            elif word[j] in temp_pointer:
                temp_pointer = temp_pointer[word[j]]
            else:
                break
    return " ".join(words)


print(
    replaceWords(
        dictionary=["cat", "bat", "rat"],
        sentence="the cattle was rattled by the battery"
    )
)
print(
    replaceWords(
        dictionary=["a","b","c"],
        sentence="aadsfasf absbs bbab cadsfafs"
    )
)
