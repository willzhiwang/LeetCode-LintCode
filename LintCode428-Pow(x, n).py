class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """

    def myPow(self, x, n):
        # write your code here

        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        num = x

        while n > 0:
            if n % 2 == 1:
                ans = ans * num
                n = n - 1
            else:
                num = num * num
                n = n // 2
        return ans