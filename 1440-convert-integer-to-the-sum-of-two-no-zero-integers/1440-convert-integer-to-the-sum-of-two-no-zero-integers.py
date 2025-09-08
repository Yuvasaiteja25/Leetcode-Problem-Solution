class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]

        for i in range(1,n):
            a=i
            b=n-i
            flag=0

            while(b!=0):
                if b%10==0:
                    flag=1
                    break
                else:
                    b=b//10
            
            if flag==1:
                continue

            flag=0
            while(a!=0):
                if a%10==0:
                    flag=1
                    break

                else:
                    a=a//10

            if flag==1:
                continue

            
            l.append(i)
            l.append(n-i)

            return l


        