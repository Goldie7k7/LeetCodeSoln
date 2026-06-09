1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n <= 2:
4            return n
5        
6        prev2, prev1 = 1, 2
7        for i in range(3, n + 1):
8            curr = prev1 + prev2
9            prev2 = prev1
10            prev1 = curr
11        
12        return prev1
13        