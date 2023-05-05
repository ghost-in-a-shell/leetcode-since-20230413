import bisect
import copy

def maxTotalFruits(fruits, startPos: int, k: int) -> int:
    fruits0=copy.deepcopy(fruits)
    fruits1=fruits[::-1]
    for i,data in enumerate(fruits1):
        fruits1[i][0]=500000-data[0]
    #return helper(fruits0,startPos,k)
    return max(helper(fruits0,startPos,k),helper(fruits1,500000-startPos,k))
def helper(fruits, startPos: int, k: int):
    start=bisect.bisect_left(fruits,[startPos])
    j=start
    lasti=-1
    window=0
    res=0
    while j<len(fruits) and fruits[j][0]-startPos<=k:
        leftbound=min(2*fruits[j][0]-startPos-k,startPos)
        i=bisect.bisect_left(fruits,[leftbound])
        if lasti<0:
            lasti=i
            for index in range(i,j+1):
                window+=fruits[index][1]
        else:
            window+=fruits[j][1]
            for index in range(lasti,i):
                window-=fruits[index][1]
            lasti=i
        res=max(window,res)
        j+=1
    return res

f=[[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
x=5
y=4
a=maxTotalFruits(f,x,y)
print(a)