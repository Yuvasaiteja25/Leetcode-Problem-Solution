class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        if min(nums)<k:
            return -1


        s=set(nums)

        if k in nums:
            return len(s)-1

        return len(s)

        