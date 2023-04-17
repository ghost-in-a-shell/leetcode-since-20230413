class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res=10000000000
        maxs=0
        for d in divisors:
            score=0
            for n in nums:
                if n%d==0:
                    score+=1
            if score>maxs:
                maxs=score
                res=d
            elif score==maxs:
                res=min(d,res)
        return res
            