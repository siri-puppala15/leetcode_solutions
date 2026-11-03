class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        def bt(re,curr,st):
            if re ==0:
                res.append(list(curr))
                return
            for i in range(st,len(candidates)):
                if re-candidates[i]<0:
                    break
                curr.append(candidates[i])
                bt(re-candidates[i],curr,i)
                curr.pop()
        bt(target,[],0)
        return res