class Solution(object):
    def partition(self, s):
        result = []
        def is_palindrome(sub):
            return sub == sub[::-1]
        def backtrack(st, c):
            if st == len(s):
                result.append(list(c))
                return
            for end in range(st + 1, len(s) + 1):
                sub = s[st:end]
                if is_palindrome(sub):
                    c.append(sub)
                    backtrack(end, c)
                    c.pop()
        backtrack(0, [])
        return result