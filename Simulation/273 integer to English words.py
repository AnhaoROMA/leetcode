"""
https://leetcode.com/problems/integer-to-english-words/

Convert a non-negative integer num to its English words representation.

Input: num = 123
Output: "One Hundred Twenty Three"

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Constraints:
    0 <= num <= 2^{31}-1
"""
data_1 = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
    "11": "Eleven",
    "12": "Twelve",
    "13": "Thirteen",
    "14": "Fourteen",
    "15": "Fifteen",
    "16": "Sixteen",
    "17": "Seventeen",
    "18": "Eighteen",
    "19": "Nineteen",
    "20+": "Twenty",
    "30+": "Thirty",
    "40+": "Forty",
    "50+": "Fifty",
    "60+": "Sixty",
    "70+": "Seventy",
    "80+": "Eighty",
    "90+": "Ninety"
}

data_2 = [
    "", "Thousand", "Million", "Billion"
]


def cut_str(s: str, cut_length: int) -> list[str]:
    result = list()
    while s:
        result = [s[-1*cut_length:]] + result
        s = s[:-1*cut_length]
    return result


def pronounce_xxx(s: str) -> str:
    if len(s) == 1:
        return data_1[s]
    elif len(s) == 2:
        # 防止出现 "00" 这种情况
        if s[0] == "0":
            if s[1] == "0":
                return ""
            else:
                return data_1[s[1]]
        if s[0] == "1":
            return data_1[s]
        else:
            if s[1] == "0":
                return data_1[s[0]+"0+"]
            else:
                return data_1[s[0]+"0+"] + " " + data_1[s[1]]
    else:
        if s[0] == "0":
            while s.startswith("0"):
                s = s[1:]
            if len(s) == 0:
                return "None"
            else:
                return pronounce_xxx(s)
        temp = data_1[s[0]] + " Hundred " + pronounce_xxx(s[1:])
        if temp.endswith(" "):
            temp = temp[:-1]
        return temp


def convert(num: int) -> str:
    num = str(num)
    parts = cut_str(num, 3)
    # print(parts)
    ans = ""
    for i in range(len(parts)):
        tmp = pronounce_xxx(parts[-1*(i+1)])
        if tmp != "None":
            ans = tmp + " " + data_2[i] + " " + ans
    while ans.endswith(" "):
        ans = ans[:-1]
    return ans


print(convert(1000))
