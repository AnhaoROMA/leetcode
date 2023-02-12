"""
https://leetcode.com/problems/longest-absolute-file-path/
"""


def lengthLongestPath(string: str) -> int:
    rows = string.split("\n")
    length = len(rows)
    dirs = [[-1, ""] for _ in range(length)]
    for i in range(length):
        temp = rows[i]
        num_levels = 0
        while temp.startswith("\t"):
            num_levels += 1
            temp = temp[1:]  # 注意 '\t' 是 1 个字符！
        dirs[i][0] = num_levels
        dirs[i][1] = temp

    del rows
    del num_levels
    del temp
    del i

    answer = 0
    cur_level = -1
    cur_path = []
    for level, name in dirs:
        while level <= cur_level:
            cur_path.pop()
            cur_level -= 1
        cur_path.append(name)
        cur_level += 1
        print("当前的文件夹名或文件名是："+"/".join(cur_path))
        if "." in name:
            # 如果现在是文件
            answer = max(answer, len("/".join(cur_path)))
        else:
            # 如果现在是文件夹
            pass
    return answer


print(
    lengthLongestPath(
        "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    )
)
print(
    lengthLongestPath(
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    )
)
print(
    lengthLongestPath(
        "a"
    )
)
