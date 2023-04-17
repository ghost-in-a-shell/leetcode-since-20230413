class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        change=[]
        maxi=0
        for i in nums:
            maxi=max(i,maxi)
            change.append(maxi+i)
        res=[]
        cur=0
        for c in change:
            cur+=c
            res.append(cur)
        return res