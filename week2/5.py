class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod = 1
        sum = 0
        while n > 0:
            prod *= n%10
            sum += n%10
            n //= 10
        return prod - sum