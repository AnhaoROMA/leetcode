"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/

You are given a string s and an array of strings words of the same length.
Return all starting indices of substring(s) in s
that is a concatenation of each word in words exactly once, in any order,
and without any intervening characters.

You can return the answer in any order.

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
"""


def find(s: str, words: list[str]) -> list[int]:
    result = list()

    uint_length = len(words[0])

    i = 0
    while i <= len(s) - len(words) * uint_length:
        count = 0
        while len(words) > 0:
            if s[i + count * uint_length: i + (count + 1) * uint_length] in words:
                words.remove(s[i + count * uint_length: i + (count + 1) * uint_length])
                count += 1
            else:
                break
        if len(words) == 0:
            result.append(i)
        while count > 0:
            words.append(s[i + (count - 1) * uint_length: i + count * uint_length])
            count -= 1
        i += 1

    return result


string = "barfoofoobarthefoobarman"
a = ["bar", "foo", "the"]
print(find(string, a))
