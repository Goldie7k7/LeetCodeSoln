1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        return bin(int(a, 2) + int(b, 2))[2:]