class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        f=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i-1] and i>0:
                continue
            
            l=i+1
            r=len(nums)-1
            while l<r:
                a=nums[i]+nums[l]+nums[r]
                if a<0:
                    l+=1
                elif a>0:
                    r-=1
                else:
                    f.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1

        return f