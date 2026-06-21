1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        i,j=0,0
4        
5        c = ''
6        while i < len(word1) and j < len(word2):
7            c = c+word1[i]+word2[j]
8            i+=1
9            j+=1
10        c += word1[i:]
11        c += word2[j:]
12        return c
13            
14        