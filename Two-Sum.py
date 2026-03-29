1class Solution:
2    def twoSum(self, nums: list[int], target: int) -> list[int]:
3        seen = {}  # Our dictionary to remember numbers: {number: index}
4        
5        for i, num in enumerate(nums):
6            complement = target - num
7            
8            # Now we need to check if the complement is in our 'seen' dictionary
9            if complement in seen:
10                # We found it! 
11                # We return the index stored in the dictionary and the current index 'i'
12                return [seen[complement], i]
13            seen[num] = i
14            # If we didn't find it, what should we do with the current 'num' 
15            # so we can find it later?