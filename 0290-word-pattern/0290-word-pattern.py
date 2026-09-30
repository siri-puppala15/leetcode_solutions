class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        t = {}
        w = {}
        for char, word in zip(pattern, words):
            if char in t and t[char] != word:
                return False
            if word in w and w[word] != char:
                return False
            t[char] = word
            w[word] = char
        return True