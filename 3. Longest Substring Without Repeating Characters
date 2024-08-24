class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        low=0
        high=0
        ans=""
        ans+=s[0]
        l=list(ans)
        maxi=len(ans)
        for i in range(1,len(s)):
            ans+=s[i]
            high+=1
            l=list(ans)
            setu=set(l)
            if len(setu)==len(l):
                maxi=max(maxi,len(ans))
            else:
                low+=1
                ans=ans[1::]
        return maxi







                
            
            

