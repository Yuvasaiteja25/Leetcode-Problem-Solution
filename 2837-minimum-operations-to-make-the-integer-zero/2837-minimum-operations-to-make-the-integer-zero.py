class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

        for k in range(1, 61):  # try up to 60 steps (enough for constraints)
            x = num1 - k * num2
            if x < 0:
                return -1
            # check if x can be written as sum of k powers of two
            if bin(x).count("1") <= k <= x:
                return k
        return -1



        