1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        res= defaultdict(list)
4        for s in strs:
5            count=[0] *26
6
7            for c in s:
8                count[ord(c)- ord("a")] +=1
9
10            res[tuple(count)].append(s)
11        return list(res.values())
12        
13                