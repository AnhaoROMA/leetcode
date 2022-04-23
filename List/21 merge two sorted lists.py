"""
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            i = list1
            j = list2
            head = i
        else:
            i = list2
            j = list1
            head = i

        aux = i
        i = aux.next
        while aux is not None:
            if i is None and j is None:
                break
            elif i is None:
                aux.next = j
                aux = aux.next
                j = j.next
            elif j is None:
                aux.next = i
                aux = aux.next
                i = i.next
            elif i.val > j.val:
                aux.next = j
                aux = aux.next
                j = j.next
            else:
                aux.next = i
                aux = aux.next
                i = i.next

        return head
