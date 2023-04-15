class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        neighbor=dict()
        #build the neighbor dict
        for path in paths:
            if max(path) not in neighbor:
                neighbor[max(path)]=[]
            neighbor[max(path)].append(min(path))
        #dye it babe!
        res=[]
        for i in range(1,n+1):
            ban=[]
            if i in neighbor:
                for node in neighbor[i]:
                    ban.append(res[node-1])
            for color in [1,2,3,4]:
                if color not in ban:
                    res.append(color)
                    break
        return res
