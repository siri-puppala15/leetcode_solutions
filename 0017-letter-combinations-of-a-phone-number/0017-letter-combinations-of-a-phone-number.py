class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        phone_map = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        s = [""]
        for i in digits:
            ns = []
            for j in s:
                for k in phone_map[i]:
                    ns.append(j + k)
            s = ns
        return s