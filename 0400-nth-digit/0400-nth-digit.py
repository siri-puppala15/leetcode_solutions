class Solution(object):
    def findNthDigit(self, n):
        l = 1
        c = 9
        s = 1
        while n > l * c:
            n -= l * c
            l += 1
            c *= 10
            s *= 10
        s += (n - 1) // l
        return int(str(s)[(n - 1) % l])