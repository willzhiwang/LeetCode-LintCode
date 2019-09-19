"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
        # return the number on given index,
        # return 2147483647 if the index is invalid.
"""


class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """

    def searchBigSortedArray(self, reader, target):
        # write your code here
        if reader is None or target is None:
            return -1
        start = 0
        end = 1
        while reader.get(end) < target:
            end = end * 2

        while start + 1 < end:
            mid = (start + end) // 2
            if target > reader.get(mid):
                start = mid
            else:
                end = mid
        if reader.get(start) == target:
            return start
        elif reader.get(end) == target:
            return end
        else:
            return -1