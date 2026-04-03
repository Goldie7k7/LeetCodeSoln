1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        check = False
4        sorteds = ''.join(sorted(s))
5        sortedt = ''.join(sorted(t))
6        if sorteds == sortedt:
7            check = True
8        return check
9            
10        