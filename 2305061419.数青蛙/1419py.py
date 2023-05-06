class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croakdict={'c':0,'r':1,'o':2,'a':3,'k':4}
        steps={0:0,1:0,2:0,3:0,4:0}
        cur=0
        res=0
        for ch in croakOfFrogs:
            if ch not in croakdict:
                return -1
            else:
                if ch=='c':
                    steps[0]+=1
                    cur+=1
                    res=max(res,cur)
                else:
                    cid=croakdict[ch]
                    if steps[cid-1]==0:
                        return -1
                    else:
                        steps[cid-1]-=1
                        steps[cid]+=1
                        if cid==4:
                            cur-=1
        #someone not finish
        if cur!=0:
            return -1
        return res