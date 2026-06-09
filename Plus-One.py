1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        s = ''
4        p =[]
5        for i in digits:
6            s = s + str(i)
7        l = int(s)+1
8        for i in str(l):
9            p.append(int(i))
10        return p
11
12        