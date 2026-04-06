1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, l1, l2):
8        if not l1: return l2
9        if not l2: return l1
10        
11        if l1.val < l2.val:
12            l1.next = self.mergeTwoLists(l1.next, l2)
13            return l1
14        else:
15            l2.next = self.mergeTwoLists(l1, l2.next)
16            return l2