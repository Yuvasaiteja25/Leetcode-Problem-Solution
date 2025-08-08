class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count=0

        for i in range(len(nums)-2):
            l=nums[i:i+3]
            if l[1]==2*(l[0]+l[2]):
                count+=1

        return count

        