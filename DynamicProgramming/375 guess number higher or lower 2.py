"""
https://leetcode.com/problems/guess-number-higher-or-lower-ii/

We are playing the Guessing Game.

The game will work as follows:
    I pick a number between 1 and n.
    You guess a number.
    If you guess the right number,
        you win the game.
    If you guess the wrong number,
        then I will tell you whether the number I picked is higher or lower,
        and you will continue guessing.
    Every time you guess a wrong number x, you will pay x dollars.
    If you run out of money, you lose the game.

Given a particular n,
return the minimum amount of money you need to guarantee a win regardless of what number I pick.

Constraints:
    1 <= n <= 200
"""


def getMoneyAmount(n: int) -> int:
    """
    在题目给的示例中，
    我们可以很明显地看到 “树 ”的结构，
    这就启发我们使用动态规划。
    """
    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][i] = 0

    def helping_hand(x: int, y: int) -> int:
        if dp[x][y] < 0:
            # 还没处理（计算）过
            tmp = x + helping_hand(x+1, y)
            tmp = min(tmp, y+helping_hand(x, y-1))
            for j in range(x+1, y):
                # i = x+1, x+2, ... , y-2, y-1
                tmp = min(tmp, j+max(helping_hand(j+1, y), helping_hand(x, j-1)))
            dp[x][y] = tmp
        return dp[x][y]

    return helping_hand(1, n)


print(getMoneyAmount(10))
print(getMoneyAmount(1))
print(getMoneyAmount(2))
