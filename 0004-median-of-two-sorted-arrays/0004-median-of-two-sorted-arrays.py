import numpy as np
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        f=0.00000
        num3=nums1+nums2
        num3.sort()
        f=np.median(num3)
        return f
