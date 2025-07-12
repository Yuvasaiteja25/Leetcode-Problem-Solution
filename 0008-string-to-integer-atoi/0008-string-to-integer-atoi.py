class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        sign_flag = None
        integer = []
        i = 0
        n = len(s)
        
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == " ":
            i += 1
        
        # Step 2: Read optional sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign_flag = s[i]
            i += 1
        
        # Step 3: Read digits
        while i < n and s[i].isdigit():
            integer.append(int(s[i]))
            i += 1
        
        # Step 4: If no digits were found, return 0
        if not integer:
            return 0
        
        # Step 5: Convert list of digits to number
        ans = 0
        for digit in integer:
            ans = ans * 10 + digit
        
        # Step 6: Apply sign
        if sign_flag == '-':
            ans *= -1
        
        # Step 7: Clamp to 32-bit signed integer range
        if ans < INT_MIN:
            return INT_MIN
        if ans > INT_MAX:
            return INT_MAX
        
        return ans
