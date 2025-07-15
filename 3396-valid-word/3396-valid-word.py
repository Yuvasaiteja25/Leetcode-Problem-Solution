class Solution:
    def isValid(self, word: str) -> bool:
        a=0
        b=0
        c=0
        d=0
        vowels="aeiouAEIOU"
        numbers="0123456789"
        if len(word)<3:
            return False

        for i in word:
            if i.isalnum():
                if i in numbers:
                    a=1

                elif i in vowels:
                    b=1

                else:
                    c=1

            else:
                return False

        
        if b+c ==2:
            return True

        return False

        