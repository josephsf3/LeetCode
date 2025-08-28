class Solution:
    def longestPalindrome(self, s: str) -> str:
        mv,ml='',0
        for k in range(len(s)):
            i=k
            j=k
            while i>=0 and j<len(s) and s[i]==s[j]:
                if j-i+1>ml:
                    ml=j-i+1
                    mv=s[i:j+1]
                i-=1
                j+=1
            i=k
            j=k+1
            while i>=0 and j<len(s) and s[i]==s[j]:
                if j-i+1>ml:
                    ml=j-i+1
                    mv=s[i:j+1]
                i-=1
                j+=1

        return mv
    
""" 
Runtime
311
ms
Beats
55.26% 
"""
