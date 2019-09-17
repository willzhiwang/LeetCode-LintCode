class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if target is None:
            return -1
        start=0
        end=len(nums)
        while (start+1<end):
            mid = start + (end-start)
            if (nums[mid] > target):
                end = mid
            if (nums[mid] < target):
                start = mid
            else:
                start = mid
            self.checktarget( target, start, end)
    def checktarget (self, target, start, end):
        if (target == end):
            return end
        elif (target == start ):
            return start
        else:
            return -1;