"""
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def find_smallest_index(self, list) -> int:
        result = 0
        temp = list[result].val
        for i in range(len(list)):
            if list[i].val < temp:
                result = i
                temp = list[i].val
        return result

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ptrs = list()
        for i in lists:
            if i is not None:
                ptrs.append(i)
        if len(ptrs) == 0:
            return None
        smallest_index = self.find_smallest_index(ptrs)
        head = ptrs[smallest_index]
        ptrs[smallest_index] = ptrs[smallest_index].next
        if ptrs[smallest_index] is None:
            ptrs.pop(smallest_index)
        cur = head

        while len(ptrs) != 0:
            smallest_index = self.find_smallest_index(ptrs)
            cur.next = ptrs[smallest_index]
            cur = cur.next
            ptrs[smallest_index] = cur.next
            if ptrs[smallest_index] is None:
                ptrs.pop(smallest_index)

        return head
