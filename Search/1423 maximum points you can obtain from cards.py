"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

There are several cards arranged in a row,
and each card has an associated number of points.
The points are given in the integer array cardPoints.

In one step,
you can take one card from the beginning or from the end of the row.
You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k,
return the maximum score you can obtain.

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12

Input: cardPoints = [2,2,2], k = 2
Output: 4

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55

Constraints:
    1 <= cardPoints.length <= 105
    1 <= cardPoints[i] <= 104
    1 <= k <= cardPoints.length
"""


# 方法一：递归
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 方法一：超时
        i = 0
        j = len(cardPoints) - 1
        if k == 1:
            return max(cardPoints[i], cardPoints[j])
        return max(
            cardPoints[i] + self.maxScore(cardPoints[i+1:], k-1),
            cardPoints[j] + self.maxScore(cardPoints[:j], k-1)
        )


# 方法二：滑动窗口的思想
# 将 左右两侧的问题 转换为 剩余的中间部分的问题
def max_score(cards: list[int], k: int) -> int:
    length = len(cards)
    # helping_hand[i] 表示 sum(cards[:i])
    helping_hand = [0 for _ in range(length + 1)]
    for i in range(1, length + 1):
        helping_hand[i] = helping_hand[i - 1] + cards[i - 1]
    # inv_ans 表示和最小的中间部分
    inv_ans = helping_hand[length - k] - helping_hand[0]
    for i in range(length - k + 1, length + 1):
        inv_ans = min(inv_ans, helping_hand[i] - helping_hand[i - length + k])
    # 由此，可计算出和最大的左右两侧
    return helping_hand[length] - helping_hand[0] - inv_ans
