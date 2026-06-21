1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        l, r = 0, len(s) - 1
4
5        while l < r:
6            if s[l] != s[r]:
7                skipL = s[l + 1 : r + 1]
8                skipR = s[l : r]
9                return skipL == skipL[::-1] or skipR == skipR[::-1]
10            l, r = l + 1, r - 1
11
12        return True