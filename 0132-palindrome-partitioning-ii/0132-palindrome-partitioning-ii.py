class Solution(object):
    def minCut(self, s):
        n = len(s)
        dp = [0] * n
        for i in range(n):
            dp[i] = i
        for i in range(n):
            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if i == 0:
                        dp[j] = 0
                    else:
                        dp[j] = min(dp[j], dp[i-1] + 1)
        return dp[n-1]