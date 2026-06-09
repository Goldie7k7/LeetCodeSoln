1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        k = 0
4        for i in nums:
5            if i != val:
6                nums[k] = i
7                k += 1
8        return k
9        