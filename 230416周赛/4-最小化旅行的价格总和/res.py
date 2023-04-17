class Solution:
    def saver(self,cur,cursave,neighbor,pre,cost):
        p2=[]
        cs1=cursave+cost[cur]/2
        cs2=cursave
        tmp=[]
        for neigh in neighbor[cur]:
            if neigh!=pre:
                tmp.append(neigh)
        p2=tmp
        for next2 in p2:
            cs2=max(cs2,self.saver(next2,cs2,neighbor,cur,cost))
        if cost[cur]==0:
            return cs2
        for t in tmp:
            for neigh in neighbor[t]:
                if neigh!=cur:
                    cs1=max(cs1,self.saver(neigh,cs1,neighbor,t,cost))
        return max(cs1,cs2)

    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        neighbor=dict()
        for i in range(n):
            neighbor[i]=[]
        times=[]
        for i in range(n):
            times.append(0)
        for e in edges:
            neighbor[e[0]].append(e[1])
            neighbor[e[1]].append(e[0])
        allpath=[]
        for t in trips:
            start=t[0]
            end=t[1]
            queue = deque()
            queue.append(start)
            predecessors = {start: None}
            while queue:
                current = queue.popleft()
                if current == end:
                    path = []
                    while current is not None:
                        path.append(current)
                        current = predecessors[current]
                    finalpath=path[::-1]
                    break
                for neigh in neighbor[current]:
                    if neigh not in predecessors:
                        predecessors[neigh] = current
                        queue.append(neigh)
            for node in finalpath:
                times[node]+=1
        cost=[]
        for i in range(n):
            cost.append(times[i]*price[i])
        for i,c in enumerate(cost):
            if c!=0:
                root=i
        save=self.saver(i,0,neighbor,-1,cost)
        return int(sum(cost)-save)