1class Solution:
2    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
3        res = {}
4        # 1. Count frequencies properly
5        for n in nums:
6            res[n] = res.get(n, 0) + 1
7        
8        # 2. Sort the dictionary items by the COUNT (item[1]) in reverse
9        # res.items() gives us (number, frequency)
10        sorted_items = sorted(res.items(), key=lambda item: item[1], reverse=True)
11        
12        # 3. Extract the first 'k' numbers (the keys)
13        result = []
14        for i in range(k):
15            result.append(sorted_items[i][0])
16            
17        return result