"""
19. Remove Nth Node From End of List (https://leetcode.com/problems/remove-nth-node-from-end-of-list)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head

        try:
            for _ in range(n+1):
                fast = fast.next

            while fast is not None:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next

            return head
        except:
            return head.next

        