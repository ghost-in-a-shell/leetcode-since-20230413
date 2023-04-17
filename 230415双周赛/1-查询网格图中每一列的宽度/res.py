class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        m=len(grid[0])
        res=[]
        for i in range (m):
            resi=0
            for j in range(n):
                cur=0
                num=grid[j][i]
                if num==0:
                    num=1
                if num<0:
                    num=-num
                    cur=1
                cur =cur+ int(math.log10(num))+1
                resi=max(resi,cur)
            res.append(resi)
        return res