class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i=='(':
                l.append(1)
            if i=='{':
                l.append(2)
            if i=='[':
                l.append(3)
            if i==')':
                if not l or l.pop()!=1:
                    return False
            if i=='}':
                if not l or l.pop()!=2:
                    return False
            if i==']':
                if not l or l.pop()!=3:
                    return False
        return False if l else True
                

""" 
Runtime

0
ms
Beats
100.00%
"""