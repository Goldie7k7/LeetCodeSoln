1class Solution:
2    def maxIceCream(self, costs: List[int], coins: int) -> int:
3        count = [0] * (max(costs) + 1)
4        s = 0
5        c = 0
6        for cost in costs:
7            count[cost] += 1
8        for i in range(1, len(count)):   # start at 1, price 0 doesn't exist
9            if count[i] == 0:
10                continue
11            if i * count[i] <= coins:    # can afford ALL bars at this price
12                coins -= i * count[i]
13                c += count[i]
14            else:                        # can only afford SOME
15                c += coins // i
16                return c                 # nothing cheaper left, stop here
17        return c
18            
19