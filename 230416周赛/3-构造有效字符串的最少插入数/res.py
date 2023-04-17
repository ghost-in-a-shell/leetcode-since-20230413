class Solution:
    def addMinimum(self, word: str) -> int:
        res=0
        l=len(word)
        p=0
        while p<l:
            if word[p]=='a':
                if p+1==l:
                    res+=2
                    break
                else:
                    p+=1
                    if word[p]=='a':
                        res+=2
                        continue
                    elif word[p]=='c':
                        res+=1
                        p+=1
                        continue
                    else:
                        if p+1==l:
                            res+=1
                            break
                        else:
                            p+=1
                            if word[p]!='c':
                                res+=1
                            else:
                                p+=1
            elif word[p]=='b':
                res+=1