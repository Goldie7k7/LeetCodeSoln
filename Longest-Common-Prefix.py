1class Solution:
2    def longestCommonPrefix(self, strs: list[str]) -> str:
3        if not strs:
4            return ""
5        
6        # Sort the strings alphabetically
7        strs.sort()
8        
9        first = strs[0]
10        last = strs[-1]
11        result = ""
12        
13        # Only compare the first and last strings
14        for i in range(len(first)):
15            if i < len(last) and first[i] == last[i]:
16                result += first[i]
17            else:
18                # Break as soon as they don't match
19                break
20                
21        return result