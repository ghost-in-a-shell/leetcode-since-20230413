class Solution:
    def longestDecomposition(self, text: str) -> int:
        res=1
        l=len(text)
        if l==0:
            return 0
        for i in range(l):
            if i>=l-i-1:
                return 1
            if text[:i+1]==text[l-i-1:]:
                return self.longestDecomposition(text[i+1:l-i-1])+2