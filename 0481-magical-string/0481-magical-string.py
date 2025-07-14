from collections import Counter
class Solution:
    def magicalString(self, n: int) -> int:
        s=[1,2,2]

        if n<=3:
            return 1



        indi=2

        while(len(s)<n):
            i=s[indi]
            if s[-1]==2:
                for j in range(i):
                    s.append(1)

            else:
                for j in range(i):
                    s.append(2)


            indi+=1

        s=s[0:n]

        d=Counter(s)

        return d[1]
