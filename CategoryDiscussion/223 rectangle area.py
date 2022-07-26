"""
https://leetcode.com/problems/rectangle-area/

Given the coordinates of two rectilinear rectangles in a 2D plane,
return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1)
and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1)
and its top-right corner (bx2, by2).

Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45

Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16
"""


def area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) -> int:
    temp = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)
    # 首先判断有没有相交部分
    if ax2 <= bx1 or bx2 <= ax1 or ay2 <= by1 or by2 <= ay1:
        return temp
    # 相交部分分成左右，上下四个点处理
    left = max(ax1, bx1)
    right = max(left, min(ax2, bx2))
    down = max(ay1, by1)
    top = max(down, min(ay2, by2))
    return temp - (top-down)*(right-left)
