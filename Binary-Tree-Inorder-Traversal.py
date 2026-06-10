1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        res = []
10        stk = []
11        cur = root
12
13        while cur or stk:
14            while cur:
15                stk.append(cur)
16                cur = cur.left
17            cur = stk.pop()
18            res.append(cur.val)
19            cur = cur.right
20        return res
21        