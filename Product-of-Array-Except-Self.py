1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        left = [1] * n
5        right = [1] * n
6        
7        # Build left products
8        for i in range(1, n):
9            left[i] = left[i-1] * nums[i-1]
10        
11        # Build right products
12        for i in range(n-2, -1, -1):
13            right[i] = right[i+1] * nums[i+1]
14        
15        # Combine
16        return [left[i] * right[i] for i in range(n)]