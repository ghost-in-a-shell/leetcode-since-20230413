class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res=[0,0]
        maxn=0
        for i,line in enumerate(mat):
            count=0
            for n in line:
                if n==1:
                    count+=1
            if count>maxn:
                maxn=count
                res=[i,maxn]
        return res
