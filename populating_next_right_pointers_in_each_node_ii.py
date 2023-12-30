'''
problem link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
'''

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = deque([root])
        while queue:
            level_size = len(queue)
            prev = None
            for i in range(level_size):
                curr = queue.popleft()
                if prev:
                    prev.next = curr
                prev = curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root
