1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        result = 0
4        for n in nums:
5            result ^= n
6        return result
7                
8        