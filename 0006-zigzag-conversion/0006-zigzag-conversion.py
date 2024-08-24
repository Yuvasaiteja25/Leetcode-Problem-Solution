class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s

        l=['']*numRows
        print(len(l))
        j=0
        k=1
        print(l)
        for i in s:
            l[j]=l[j]+i
            if(j==0):
                k=1
            if(j==numRows-1):
                k=0
            if(k==1):
                j+=1
            if(k==0):
                j-=1
        ans=''
        for i in l:
            ans+=str(i)
        return ans



        