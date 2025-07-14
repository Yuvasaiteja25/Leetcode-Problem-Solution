class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        l=[]
        for i in range(len(weights)-1):
            t=weights[i]+weights[i+1]
            l.append(t)


        l.sort()

        mini=0
        maxi=0

        for i in range(k-1):
            mini+=l[i]

        l=l[::-1]

        for i in range(k-1):
            maxi+=l[i]


        return maxi-mini
        

