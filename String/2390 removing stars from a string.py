def remove(s: str) -> str:
    char_stack = []

    for char in s:
        if char == "*":
            char_stack.pop()
        else:
            char_stack.append(char)

    return "".join(char_stack)


print(remove("leet**cod*e"))
print(remove("erase*****"))
