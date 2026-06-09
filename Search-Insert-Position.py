1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        if target in nums:
4            return nums.index(target)
5        elif target not in nums:
6            nums.append(target)
7            sort = sorted(nums)
8            return sort.index(target)
9        