class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = []
        
        @lru_cache(None)
        def dfs(co,cc,v):
            if co == cc and co + cc == n * 2:
                l.append(v)
                return
            if co < n:
                dfs(co + 1, cc, v + '(')
            if cc < co:
                dfs(co, cc + 1, v + ')')
        dfs(0,0,'')
        return l
            

"""
Runtime

2
ms
Beats
34.18% 
"""