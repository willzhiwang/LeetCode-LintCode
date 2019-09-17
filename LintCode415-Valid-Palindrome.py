class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        if (source == None or target ==None):
            return -1
        s_l = len (source)
        t_l = len (target)
        for i in range(s_l+1-t_l):
            j=0
            while (j <t_l):
                if (source[i+j] != target[j]):
                    break
                j+=1
                if (t_l==j): #all cases matched
                    return i
        return -1