class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left=0
        right=len(nums)-1
        l=[-1,-1]
        if target not in nums:
            return l

        index=0


        while left<=right:
            mid=(left+right)//2

            if nums[mid]==target:
                index=mid
                break

            elif nums[mid]<target:
                left=mid+1

            else:
                right=mid-1

        last=index
        for i in range(index+1,len(nums)):
            if nums[i]==target:
                last+=1

            else:
                break

        first=index
        for i in range(index-1,-1,-1):
            if nums[i]==target:
                first-=1

            else:
                break


        l[0]=first
        l[1]=last

        return l







        