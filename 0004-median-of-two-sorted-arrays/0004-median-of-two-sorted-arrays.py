class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        num=nums1+nums2
        num.sort()

        if len(num)%2 == 0:
            x=len(num)//2
            return (num[x] + num[x-1])/2

        x=len(num)//2
        return num[x]
        