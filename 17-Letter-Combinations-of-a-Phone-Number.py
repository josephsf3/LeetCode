class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        d={
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }

        f=[]
        l=[int(i) for i in digits]
        def solve(n, s):
            if n == len(digits):
                f.append(s)
                return 
            for i in d[l[n]]:
                solve(n+1, s+i)
        
        solve(0, '')
        return f
    


"""
Runtime

0
ms
Beats
100.00%

"""
