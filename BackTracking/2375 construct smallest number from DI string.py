def smallest_number(pattern: str):
    length = len(pattern) + 1
    result = [0 for _ in range(length)]

    def possible(pos, visited):
        if pos == length:
            return True
        last_value = result[pos-1]
        if pattern[pos-1] == "I":
            for tmp in range(last_value+1, 10):
                if tmp in visited:
                    continue
                result[pos] = tmp
                if possible(pos+1, visited+[tmp]):
                    return True
            return False
        else:
            for tmp in range(1, last_value):
                if tmp in visited:
                    continue
                result[pos] = tmp
                if possible(pos+1, visited+[tmp]):
                    return True
            return False

    for head in range(1, 10):
        result[0] = head
        if possible(1, [head]):
            break
        else:
            continue

    # return result
    ans = ""
    for num in result:
        ans += str(num)
    return ans


print(smallest_number("IDDD"))
