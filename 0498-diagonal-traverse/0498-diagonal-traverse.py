class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """

        row = len(mat)
        col = len(mat[0])

        res = []
        up = True

        cr, cl = 0, 0

        while len(res) < row * col:
            if up:
                while cr >= 0 and cl < col:
                    res.append(mat[cr][cl])
                    cr -= 1
                    cl += 1

                # fix boundary adjustments
                if cl >= col:
                    cr += 2
                    cl = col - 1
                elif cr < 0:
                    cr = 0

                up = False

            else:
                while cl >= 0 and cr < row:
                    res.append(mat[cr][cl])
                    cl -= 1
                    cr += 1

                # fix boundary adjustments
                if cr >= row:
                    cl += 2
                    cr = row - 1
                elif cl < 0:
                    cl = 0

                up = True

        return res
