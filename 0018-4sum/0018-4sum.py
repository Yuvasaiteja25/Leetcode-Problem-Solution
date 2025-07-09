class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l=[]

        n=len(nums)

        for i in range(n-3):
            for j in range(i+1,n-2):
                a=j+1
                b=n-1
                
                while(a<b):
                    ans=[]
                    s=nums[i]+nums[j]+nums[a]+nums[b]

                    if s==target:
                        ans.append(nums[i])
                        ans.append(nums[j])
                        ans.append(nums[a])
                        ans.append(nums[b])
                        ans.sort()
                        if ans not in l:
                            l.append(ans)
                        a+=1
                        b-=1

                    elif s< target:
                        a+=1

                    else:
                        b-=1

        return l

        