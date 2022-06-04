import math
"""
https://leetcode.com/problems/text-justification/

Given an array of strings words and a width maxWidth,
format the text such that
each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach;
that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line does not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text,
it should be left-justified and no extra space is inserted between words.

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."],
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Input:
words = [
    "Science","is","what","we","understand","well","enough","to",
    "explain","to","a","computer.","Art","is","everything","else","we","do"
],
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Input:
words = ["What","must","be","acknowledgment","shall","be"],
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
"""


def text_justification(words: list[str], max_width: int) -> list[str]:
    result = list()
    for word in words:
        if result and len(result[-1]) + len(word) < max_width:
            result[-1] += " "
            result[-1] += word
        else:
            result.append("")
            result[-1] += word
    # print(result)
    for i in range(len(result)):
        result[i] = result[i].split()
    # print(result)
    for i in range(len(result)):
        # 处理每一“行”
        num_words = len(result[i])  # 该行有几个单词
        len_words = 0
        for word in result[i]:
            len_words += len(word)
        # len_words：该行的单词长度之和
        num_space = max_width - len_words  # 该行总共有几个空格
        if num_words == 1:
            num_block = 1
        else:
            num_block = num_words - 1
        # num_block：该行有几个空格段

        # 将若干单词合成一个字符串
        temp_result = ""
        for word in result[i]:
            temp_result += word
            if num_block == 0:
                break
            length_of_this_block = math.ceil(num_space / num_block)
            temp_result += " "*length_of_this_block
            num_space -= length_of_this_block
            num_block -= 1
        result[i] = temp_result

    # 单独处理最后一行
    result[-1] = result[-1].split()
    temp_result = ""
    for word in result[-1]:
        temp_result += word
        temp_result += " "
    temp_result = temp_result[:-1]
    length_of_this_block = max_width - len(temp_result)
    temp_result += " "*length_of_this_block
    result[-1] = temp_result
    return result


a = ["This", "is", "an", "example", "of", "text", "justification."]
b = 16
print(text_justification(a, b))
