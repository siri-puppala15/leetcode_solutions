class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        def bt(re,curr,st):
            if re ==0:
                res.append(list(curr))
                return
            for i in range(st,len(candidates)):
                if i>st and candidates[i]==candidates[i-1]:
                    continue
                if re-candidates[i]<0:
                    break
                curr.append(candidates[i])
                bt(re-candidates[i],curr,i+1)
                curr.pop()
        bt(target,[],0)
        return res

        