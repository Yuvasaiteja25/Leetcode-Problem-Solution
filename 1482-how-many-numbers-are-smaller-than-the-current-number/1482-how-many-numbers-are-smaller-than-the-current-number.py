class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        k=sorted(nums)
        ans=[]


        for i in nums:
            n=k.index(i)  #4
            ans.append(n)

        return ans

        