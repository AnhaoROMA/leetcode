"""
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""

"""
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""


def zigzag(s: str, rows: int) -> str:
    batch = rows + rows - 2
    length = len(s)

    if batch == 0:
        return s

    batch_num = int(length / batch) + 1
    result = ""
    i = 0
    for j in range(batch_num):
        index = j * batch + i
        if index >= length:
            pass
        else:
            result += s[index]
    for i in range(1, int(batch/2)):
        for j in range(batch_num):
            index1 = j * batch + i
            if index1 >= length:
                pass
            else:
                result += s[index1]
            index2 = j * batch + (batch-i)
            if index2 >= length:
                pass
            else:
                result += s[index2]
    i = int(batch/2)
    for j in range(batch_num):
        index = j * batch + i
        if index >= length:
            pass
        else:
            result += s[index]
    return result


string = "PAYPALISHIRING"
num_rows = 4
print(zigzag(s=string, rows=num_rows))
