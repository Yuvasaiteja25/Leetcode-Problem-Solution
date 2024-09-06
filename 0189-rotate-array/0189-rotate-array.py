class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''l1=nums[-k::]
        print(l1)
        m=len(nums)-k
        l2=nums[0:m]
        l1+=l2
        for i in range(len(nums)):
            nums[i]=l1[i]'''

        nums[:] = nums[-k%len(nums):] + nums[:-k%len(nums)]
