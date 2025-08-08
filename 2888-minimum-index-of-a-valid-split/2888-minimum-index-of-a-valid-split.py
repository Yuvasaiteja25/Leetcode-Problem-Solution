from collections import Counter 
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        d=Counter(nums)
        print(d)
        f=0
        maxi=0

        for i in d:
            if d[i]>f:
                f=d[i]
                maxi=i

        print(maxi,f)
        f1,f2=0,0

        for i in range(len(nums)-1):
            if nums[i]==maxi:
                f1+=1

            f2=f-f1
            

            if 2*f1>i+1 and 2*f2>len(nums)-i-1:
                return i


        return -1




        