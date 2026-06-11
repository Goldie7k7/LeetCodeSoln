1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        nums = set(nums)
4        best = 0
5        for x in nums:
6            if x - 1 not in nums:
7                y = x + 1
8                while y in nums:
9                    y += 1
10                best = max(best, y - x)
11        return best
12
13        