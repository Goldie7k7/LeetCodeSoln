1class Solution:
2    def isValid(self, s: str) -> bool:
3        save = []
4        for i in s:
5            if i in "({[":
6                save.append(i)
7            elif i == ")":
8                # Check: Is it empty OR the wrong match?
9                if not save or save.pop() != "(":
10                    return False
11            elif i == "}":
12                if not save or save.pop() != "{":
13                    return False
14            elif i == "]":
15                if not save or save.pop() != "[":
16                    return False
17        
18        # At the end, if the stack is empty, it's valid!
19        return len(save) == 0