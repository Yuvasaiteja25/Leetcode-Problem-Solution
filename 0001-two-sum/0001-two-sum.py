class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=sorted(nums)
        l1=[]
        l=0
        r=len(nums)-1
        while(l<r):
            if n[l]+n[r] == target:
                l1.append(n[l])
                l1.append(n[r])
                break
            elif n[l]+n[r] < target:
                l+=1
            else:
                r-=1
        l2=[]
        l2.append(nums.index(l1[0]))
        l2.append(nums.index(l1[1]))
        return l2

