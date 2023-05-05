class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        last=0
        maxval=-1
        res=777
        for log in logs:
            t=log[1]-last
            last=log[1]
            if t>maxval or (t==maxval and log[0]<res):
                res=log[0]
                maxval=t
        return res