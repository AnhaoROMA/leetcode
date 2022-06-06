"""
https://leetcode.com/problems/simplify-path/

Given a string path,
which is an absolute path (starting with a slash '/') to a file or directory
in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory,
a double period '..' refers to the directory up a level,
and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'.
For this problem,
any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path
from the root directory to the target file or directory
(i.e., no period '.' or double period '..')
Return the simplified canonical path.

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op,
as the root level is the highest level you can go.

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path,
multiple consecutive slashes are replaced by a single one.
"""


def simplify_path(path: str) -> str:
    parts = path.split("/")
    i = len(parts) - 1
    while i >= 0:
        if len(parts[i]) == 0:
            parts.pop(i)
        i -= 1
    # print(parts) ---> ['home', '..', 'foo']
    result_list = list()
    for dir in parts:
        if dir == ".":
            continue
        elif dir == "..":
            if result_list:
                result_list.pop()
        else:
            result_list.append(dir)
    # print(result_list)
    result = ""
    for dir in result_list:
        result += "/"
        result += dir
    if len(result) > 0:
        return result
    else:
        return "/"


a = "/home/"
print(simplify_path(a))
