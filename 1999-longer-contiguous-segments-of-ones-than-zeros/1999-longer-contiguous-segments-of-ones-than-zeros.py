class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones=0
        zero=0
        o=0
        z=0

        for i in s:
            if i=='1':
                o+=1
                zero=max(zero,z)
                z=0

            elif i=='0':
                z+=1
                ones=max(o,ones)
                o=0


        ones=max(o,ones)
        zero=max(z,zero)

        if ones>zero:
            return True

        return False

        print(ones,zero)
