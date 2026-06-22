1class Solution:
2    def maxNumberOfBalloons(self, text: str) -> int:
3        count = {}
4        for char in text:
5            count[char] = count.get(char, 0) + 1
6        
7        return min(
8            count.get('b', 0),
9            count.get('a', 0),
10            count.get('l', 0) // 2,
11            count.get('o', 0) // 2,
12            count.get('n', 0)
13        )
14        
15  
16        