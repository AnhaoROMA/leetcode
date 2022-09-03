"""
https://leetcode.com/problems/keys-and-rooms/
"""


def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
    length = len(rooms)
    visited = [False for _ in range(length)]
    keys_on_hand = [0]
    while keys_on_hand:
        key = keys_on_hand.pop()
        visited[key] = True
        for another_key in rooms[key]:
            if visited[another_key]:
                continue
            else:
                keys_on_hand.append(another_key)
    if visited.count(True) < length:
        return False
    else:
        return True


print(can_visit_all_rooms([[1], [2], [3], []]))
print(can_visit_all_rooms([[1, 3], [3, 0, 1], [2], [0]]))
