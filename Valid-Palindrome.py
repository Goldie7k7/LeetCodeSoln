1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s1=''
4        
5        for i in s:
6            if i.isalpha():
7                s1 = s1+i
8        s = s1.lower()
9        rev = s[::-1]
10        if rev == s:
11            return True
12        else:
13            return False
14            
15                
16        
17        