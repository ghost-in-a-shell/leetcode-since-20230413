class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res=[]
        for target in queries:
            i=0
            resi=True
            for ch in target:
                if i<len(pattern) and ch==pattern[i]:
                    i+=1
                elif ord(ch)<91:
                    resi=False
            if i<len(pattern):
                resi=False
            res.append(resi)
        return res                