1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        s = s.strip().split()
4        l = len(s[-1])
5        return l
6        