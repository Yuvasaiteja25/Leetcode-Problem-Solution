from collections import Counter
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=Counter(nums)
        for i in d:
            if d[i]>=2:
                return i
        