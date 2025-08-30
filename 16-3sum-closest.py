class Solution:
    def threeSumClosest(self, n: List[int], target: int) -> int:
        s=float('inf')
        n.sort()
        for i in range(len(n)-2):
            if n[i]==n[i-1] and i>0:
                continue
            j=i+1
            k=len(n)-1
            while j<k:
                t=n[i]+n[j]+n[k]
                if abs(t-target)<abs(s-target):
                    s=t
                if t<target:
                    j+=1
                elif t>target:
                    k-=1
                else:
                    return t
                '''while n[j]==n[j-1] and j<k:
                        j+=1'''
        return s