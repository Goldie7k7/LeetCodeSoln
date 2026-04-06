1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if not nums:
4            return 0
5        
6        # 'k' acts as the pointer for the last unique element found
7        k = 0
8        
9        for i in range(1, len(nums)):
10            if nums[i] != nums[k]:
11                k += 1          # Move the unique boundary forward
12                nums[k] = nums[i] # Overwrite the next spot with the new unique value
13        
14        # The number of unique elements is k + 1
15        return k + 1