"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
"""


def cal(string: str) -> str:
    result = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    for digit in string:
        result[digit] = result[digit] + 1
    result_string = ""
    for d in result:
        result_string += str(result[d])
        result_string += "#"
    result_string = result_string[0:-1]
    return result_string


def group_anagrams(strs: list[str]) -> list[list[str]]:
    dictionary = dict()
    for string in strs:
        tmp = cal(string)
        if tmp in dictionary:
            dictionary[tmp].append(string)
        else:
            dictionary[tmp] = [string]
    result = list()
    for tmp in dictionary:
        result.append(dictionary[tmp])
    return result


strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strings))
