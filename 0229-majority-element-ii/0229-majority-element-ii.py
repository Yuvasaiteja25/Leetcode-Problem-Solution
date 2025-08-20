from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n=len(nums)//3
        d=Counter(nums)

        l=[]

        for i in d:
            if d[i]>n:
                l.append(i)

        return l