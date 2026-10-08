class Solution(object):
    def reversePrefix(self, s, k):
        s_list = list(s)
        s_list[:k] = reversed(s_list[:k])
        return "".join(s_list)