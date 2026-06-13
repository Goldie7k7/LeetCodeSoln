1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        l, r = 0, len(height) - 1
4        max_area = 0
5        while l < r:
6            area = min(height[l], height[r]) * (r - l)
7            max_area = max(max_area, area)
8            if height[l] < height[r]:
9                l += 1
10            else:
11                r -= 1
12        return max_area