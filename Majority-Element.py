1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        nums.sort()
4        return nums[len(nums) // 2]
5        