class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res=max(nums)
        maxi,mini=1,1

        for i in nums:
            if i==0:
                maxi,mini=1,1
            tmp=i*maxi
            maxi=max(i*maxi,i*mini,i)
            mini= min(tmp,i*mini,i)

            res=max(maxi,res)
        return res
        