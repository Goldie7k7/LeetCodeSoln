1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        t = []
5
6        for i in range(len(nums) - 2):
7            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates
8                continue
9
10            l, r = i + 1, len(nums) - 1
11            while l < r:
12                curr = nums[i] + nums[l] + nums[r]
13                if curr == 0:
14                    t.append([nums[i], nums[l], nums[r]])
15                    while l < r and nums[l] == nums[l + 1]:  # skip duplicates
16                        l += 1
17                    while l < r and nums[r] == nums[r - 1]:  # skip duplicates
18                        r -= 1
19                    l += 1
20                    r -= 1
21                elif curr < 0:
22                    l += 1
23                else:
24                    r -= 1
25        return t