1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        palindrome = False
4        x = str(x)
5        reverse = x[::-1]
6        if reverse == x:
7            palindrome = True
8        return palindrome
9        