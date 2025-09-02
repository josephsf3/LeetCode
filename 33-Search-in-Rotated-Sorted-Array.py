class Solution:
    def search(self, n: List[int], k: int) -> int:
        if k in n:
            return n.index(k)
        else:
            return -1


"""
Runtime
0
ms
Beats
100.00%
"""