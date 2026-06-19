1class MyHashSet:
2    def __init__(self):
3        self.size = 1000
4        self.buckets = [[] for _ in range(self.size)]
5
6    def _hash(self, key):
7        return key % self.size
8
9    def add(self, key: int) -> None:
10        i = self._hash(key)
11        if key not in self.buckets[i]:
12            self.buckets[i].append(key)
13
14    def remove(self, key: int) -> None:
15        i = self._hash(key)
16        if key in self.buckets[i]:
17            self.buckets[i].remove(key)
18
19    def contains(self, key: int) -> bool:
20        i = self._hash(key)
21        return key in self.buckets[i]