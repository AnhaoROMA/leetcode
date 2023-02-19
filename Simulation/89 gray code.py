"""
https://leetcode.com/problems/gray-code/

An n-bit gray code sequence is a sequence of 2^n integers where:
    Every integer is in the inclusive range [0, 2^n - 1];
    The first integer is 0;
    An integer appears no more than once in the sequence;
    The binary representation of every pair of adjacent integers differs by exactly one bit;
    The binary representation of the first and last integers differs by exactly one bit;

Given an integer n, return any valid n-bit gray code sequence.

Constraints:
    1 <= n <= 16
"""


def grayCode(n: int) -> list[int]:
    """
    当 n = 4 时，
    0000 -> 0001
        -> 0011 -> 0010
            -> 0110 -> 0111 -> 0101 -> 0100
                -> 1100 -> 1101 -> 1111 -> 1110 -> 1010 -> 1011 -> 1001 -> 1000

    当 n = 5 时，
    00000 -> 00001
        -> 00011 -> 00010
            -> 00110 -> 00111 -> 00101 -> 00100
                -> 01100 -> 01101 -> 01111 -> 01110 -> 01010 -> 01011 -> 01001 -> 01000
                    -> 11000 -> 11001 -> 11011 -> 11010 -> 11110 -> 11111 -> 11101 -> 11100 \
                    -> 10100 -> 10101 -> 10111 -> 10110 -> 10010 -> 10011 -> 10001 -> 10000

    很明显，假如
        grayCode(n) = A  # <-- A[i] 均为二进制！
    则
        grayCode(n+1) = A + ["1"+A[i]]
    """

    count = 1
    answer = ["0", "1"]
    while count < n:
        length = len(answer)
        temp = answer[::-1]
        for i in range(length):
            answer[i] = "0" + answer[i]
            temp[i] = "1" + temp[i]
        answer = answer + temp
        count += 1
    # print(answer)
    result = [-1 for _ in range(2**n)]
    for i in range(2**n):
        result[i] = int(answer[i], 2)
    return result


print(grayCode(2))
print(grayCode(4))
