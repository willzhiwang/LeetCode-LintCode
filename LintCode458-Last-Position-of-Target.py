class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def lastPosition(self, nums, target):
        # write your code here
        if not nums or target is None:
            return -1
        # self.target = target
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            # mid = start + (end - start) // 2
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        else:
            return -1 