class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        need=nums[0]
        moves=0
        for i in nums:
            if i<need:
                moves+=need-i

            else:
                need=i
            need+=1
        return moves
        
            
            
        