class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=[]
        ans=[]
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1

            while(j<k):
                s= nums[i]+nums[j]+nums[k]
                diff=s-target
                ans.append(s)
                l.append(abs(diff))
                if diff < 0:
                    j+=1
                    
                elif diff>0:
                    k-=1

                else:
                    return s
        
        k=l.index(min(l))
        return ans[k]


        