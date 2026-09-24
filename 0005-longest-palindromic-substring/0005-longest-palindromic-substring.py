class Solution(object):
    def longestPalindrome(self, s):
        ans = ""
        for i in range(len(s)):
            l = r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                l -= 1
                r += 1
            t = ""
            for j in range(l+1,r):
                t += s[j]
            if len(ans)<r-l-1:
                ans = t
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l -= 1
                r += 1
            t = ""
            for j in range(l+1,r):
                t += s[j]
            if len(ans)<r-l-1:
                ans = t
        return ans