class Solution:
    def findComplement(self, num: int) -> int:
        n=bin(num).split('b')
        n=n[1]
        s=''
        for i in n:
            if i=='0':
                s+='1'
            else:
                s+='0'
        return(int(s,2))
         
        
        
        return 0