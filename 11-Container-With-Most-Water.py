class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        m=0
        f=max(h)
        while l<r:
            c=min(h[l],h[r])*(r-l)
            m=max(m,c)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
            if f * (r - l) <= m:
                break
        return m
    

""" 
Runtime

6
ms
Beats
99.38%
"""


class Solution:
    def maxArea(self, h: List[int]) -> int:
        m=0
        l=0
        r=len(h)-1
        while l<r:
            m=max(m,min(h[l],h[r])*(r-l))
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return m
    
""" 
Runtime

108
ms
Beats
30.30%
"""