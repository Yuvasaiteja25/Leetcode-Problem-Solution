class Solution:
    def addBinary(self, a: str, b: str) -> str:

        m=int(a,2)
        n=int(b,2)
        ans=m+n
        ans=bin(ans)
        return ans[2::]
        