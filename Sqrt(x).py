1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x == 0:
4            return 0
5        
6        result = 0
7        for i in range(1, x + 1):
8            if i * i == x:
9                return i
10            elif i * i > x:
11                return result
12            result = i