"""
876. Middle of the Linked List (https://leetcode.com/problems/middle-of-the-linked-list)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        p = head

        while p is not None:
            length += 1
            p = p.next

        for _ in range(length // 2):
            head = head.next

        return head
