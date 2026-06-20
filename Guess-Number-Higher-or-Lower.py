1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        l = 1
11        r = n
12        
13        while l <= r:
14            num = (l + r) // 2
15            result = guess(num)  # store it once
16            if result == 0:
17                return num
18            elif result == 1:
19                l = num + 1
20            else:
21                r = num - 1
22            