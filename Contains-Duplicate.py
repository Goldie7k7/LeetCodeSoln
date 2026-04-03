1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        checkSET = set()
4        duplicate = False
5        for i in nums:
6            if i in checkSET:
7                duplicate=True
8            else:
9                checkSET.add(i)
10                
11        return duplicate
12        