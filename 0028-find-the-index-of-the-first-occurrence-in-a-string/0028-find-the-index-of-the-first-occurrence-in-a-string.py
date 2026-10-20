class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0       
        h_len, n_len = len(haystack), len(needle)    
        for i in range(h_len - n_len + 1):
            j = 0
            while j < n_len and haystack[i + j] == needle[j]:
                j += 1
            if j == n_len:
                return i
        return -1