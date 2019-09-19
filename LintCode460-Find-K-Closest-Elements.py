class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        # write your code here

        if not A:
            return []

        start = 0
        end = len(A) - 1
        result = []

        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        while len(result) < k:
            if end >= len(A) or abs(A[start] - target) <= abs(A[end] - target):
                result.append(A[start])
                start -= 1
            else:
                result.append(A[end])
                end += 1
        return result