class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        x = 0
        y = 0
        for i in range(len(gain)):
            for j in range(0, i+1):
                y += gain[j]
            if x < y:
                x = y
            y = 0
        return x