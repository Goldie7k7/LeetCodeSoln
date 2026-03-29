1class Solution:
2    def romanToInt(self, s: str) -> int:
3        dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
4        val = 0
5        for i in range(len(s)-1):
6            if dict[s[i]] < dict[s[i+1]]:
7                val-= dict[s[i]]
8            else:
9                val+=dict[s[i]]
10        return val + dict[s[-1]]
11
12
13        