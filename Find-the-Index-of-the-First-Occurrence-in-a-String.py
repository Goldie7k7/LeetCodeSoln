1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        for i in haystack:
4            if needle in haystack:
5                return haystack.index(needle)
6            else:
7                return -1
8        