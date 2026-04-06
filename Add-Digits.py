1class Solution:
2    def addDigits(self, num: int) -> int:
3        while len(str(num)) >1:
4            sum=0
5            for i in str(num):
6                sum+=int(i)
7            num=sum
8
9        return num
10        