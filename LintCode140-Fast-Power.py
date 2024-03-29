class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        ans = 1
        while n > 0:
            if (n % 2 == 1):
                ans = (ans * a) % b
                n = n - 1
            else:
                a = (a * a) % b
                n = n//2

        return ans % b