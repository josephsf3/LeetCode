class Solution:
    def divide(self, dd: int, d: int) -> int:
        a=dd/d
        if a> 2**31 -1 or a < -2**31 -1:
            return 2**31-1
        return floor(a) if a>=0 else ceil(a)
    

"""
Runtime

0
ms
Beats
100.00%

"""