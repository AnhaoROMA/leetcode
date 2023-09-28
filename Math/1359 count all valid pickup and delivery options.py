"""
https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

Given n orders, each order consist in pickup and delivery services.

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).

Since the answer may be too large, return it modulo 10^9+7.

Input:
    n = 1
Output:
    1
Explanation:
    Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

Input:
    n = 2
Output:
    6
Explanation:
    All possible orders:
        (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
        This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

Input:
    n = 3
Output:
    90

Constraints:
    1 <= n <= 500
"""


def countOrders(n: int) -> int:
    """
    找规律

    当 n = 1 时，
        仅有 P1D1 这一种可能。

    当 n = 2 时，
        若把 P2 插入 n=1 的结论，则有以下三种情况：
        1. P2P1D1
            此时 D2 有三个位置可以插入。
        2. P1P2D1
            此时 D2 有两个位置可以插入。
        3. P1D1P2
            此时 D2 有一个位置可以插入。
        综上所述，共有 3+2+1 种可能。

    当 n = 3 时，
        对于 n=2 的结论，即 6 种可能的每一种，都有如下情况（这里以 P1P2D1D2 为例）：
        1. P3-P1P2D1D2
            此时 D3 有五个位置可以插入。
        2. P1-P3-P2D1D2
            此时 D3 有四个位置可以插入。
        3. P1P2-P3-D1D2
            此时 D3 有三个位置可以插入。
        4. P1P2D1-P3-D2
            此时 D3 有两个位置可以插入。
        5. P1P2D1D2-P3
            此时 D3 有一个位置可以插入。
        综上所述，共有 6*（5+4+3+2+1）= 90 种可能。

    找到规律：
        A_1 = 1
        A_2 = A_1 * ( sum_{1}^{2*2-1} ) = 6
        A_3 = A_2 * ( sum_{1}^{2*3-1} ) = 90
        A_4 = A_3 * ( sum_{1}^{2*4-1} ) = 2520
        ... ... ...
        A_n = A_{n-1} * ( sum_{1}^{2*n-1} ) = A_{n-1} * ( 2n^2 - n )
    """
    answer = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        answer[i] = answer[i-1]*(2*i*i-i)
        answer[i] %= 10**9+7
    return answer[n]


print(countOrders(2))
print(countOrders(3))
print(countOrders(4))
print(countOrders(8))
