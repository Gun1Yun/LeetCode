"""
116. Populating Next Right Pointers in Each Node (https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        idx = 1
        cnt = 0

        queue = deque()
        if root:
            queue.append(root)

        while queue:
            cur = queue.popleft()
            cnt+=1
            if cnt == idx:
                idx*=2
            else:
                prev.next = cur
            prev = cur  
            
            if cur.left:
                queue.append(cur.left)
                queue.append(cur.right)

        return root