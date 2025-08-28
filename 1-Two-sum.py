class Solution(object):
    def twoSum(self, n, target) :
        l={}
        for i,a in enumerate(n) :
            c=target-a
            if c in l:
                return [l[c] , i]
            l[a]=i
               


""" 
Runtime
43ms
Beats
48.74%
 """