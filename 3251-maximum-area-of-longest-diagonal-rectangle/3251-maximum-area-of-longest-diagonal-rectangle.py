import math

class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_diag = 0
        max_area = 0
        
        for l, w in dimensions:
            diag = math.sqrt(l * l + w * w)
            area = l * w
            
            # Update if we find a longer diagonal,
            # or same diagonal but larger area
            if diag > max_diag or (diag == max_diag and area > max_area):
                max_diag = diag
                max_area = area
        
        return max_area
