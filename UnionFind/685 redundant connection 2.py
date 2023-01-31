"""
https://leetcode.com/problems/redundant-connection-ii/description/
"""


def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    """
    简单一点的版本是 684 题。

    那道题给的是无向图，所以去掉环里的哪条边都是可以的，归根到底就是检测环就行了。

    而这道题给的是有向图。
    即使加上当前边就发现了环（这里的环不考虑边的方向），
    也不能判断是否应该去掉当前边（因为有可能去掉当前边之后，其作为无向图确实是树，但是作为有向图依然不是有根树）。

    由题意，该图是一棵有根树加上一条边。

    那么，一棵有根树加上一条边，有哪些情况呢？
    1、一是从其中一个顶点到另外一个非树根的顶点加上一条边，那么就会产生某个顶点有两个父亲。
        这种情况下，只需要将那个有两个父亲的顶点删去那个下标较大的成环的入边即可（这里的环也是指无向图的环）。
    2、二是从其中一个顶点到树根加上一条边，此时每个顶点仍然只有一个父亲。
        这种情况下，图里一定有环（从树根先走到那个顶点，然后又回到树根），环的任意一条边删去都是可以的。

    所以算法的设计如下。
    先统计一下每个顶点的父亲是谁。
    如果统计都某一时刻发现某个顶点有两个父亲，那么这个顶点的两条入边就是备选答案，我们先将其存起来。
    注意，此时还不能判断这两个哪个是解，也有可能都是合法解。（ 因为有可能还存在双向边 i <--> j 。）
    同时，将其中一条边断开（代码里直接标记一下这条边不可用即可）。这里断开的目的是为了区分两条边哪个是成环的边。

    接着开个并查集，将原图视为无向图。
    依次 unionfind 每条边的两个顶点（略过不可用的边）。
    一旦发现某次 unionfind 的时候，两个顶点已经处于同一个集合了，那么就说明产生了环。
    我们先查一下备选解有多少个。
    如果之前没有存备选解，则说明没有顶点有两个父亲，那么此时成环的边就是当前边，直接返回当前边即可；
    如果有备选解，那么答案就是备选解里没标记断开的那个（说明没断开的那个成环了）。

    遍历完毕之后如果没 return ，则说明被断开的那条边是成环的，将其返回。
    """
    n = len(edges)
    parents = {i: -1 for i in range(1, n+1)}
    result = []
    for i in range(n):
        u, v = edges[i]
        if parents[v] > 0:
            # 如果某个节点有两个父亲，则将这两条边都存起来，并断开其中一条。
            result.append([parents[v], v])
            result.append([u, v])
            edges.pop(i)
            break
        parents[v] = u
    del parents
    del i, u, v

    union_find = {i: i for i in range(1, n+1)}

    def find(x):
        if union_find[x] != x:
            union_find[x] = find(union_find[x])
        return union_find[x]

    def merge(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        else:
            union_find[px] = py
            return True

    for u, v in edges:
        # 如果 from 和 to 已经被 merge 成一体了（说明有环），那么查一下备选答案。
        # 如果备选答案为空，则返回最后一个成环的边，即当前边。（情况二）
        # 否则，备选答案里没有断开的那条边就是答案。（断掉的那条边并不是“罪魁祸首”）
        if merge(u, v) is False:
            if not result:
                return [u, v]
            else:
                return result[0]

    # 如果除了刚刚我们断掉的那条边，其余所有的边都不成环，那么断掉的那条边就是“罪魁祸首”，故返回之。
    return result[1]


print(
    findRedundantConnection(
        [[2, 1], [3, 1], [4, 2], [1, 4]]
    )
)
print(
    findRedundantConnection(
        [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
    )
)
print(
    findRedundantConnection(
        [[1, 2], [1, 3], [2, 3]]
    )
)
