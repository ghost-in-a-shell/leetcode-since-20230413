class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n=len(arr1)
        m=min(len(arr2),n)+1
        maxval=10**9+1
        dp=[[maxval for _ in range(m)] for _ in range(n+1)]
        dp[0][0]=-1
        for i in range(1,n+1):
            for j in range(min(m,i+1)):
                if arr1[i-1]>dp[i-1][j]:
                    dp[i][j]=arr1[i-1]
                if j>0:
                    index=bisect.bisect_right(arr2,dp[i-1][j-1])
                    if index<len(arr2):
                        dp[i][j]=min(dp[i][j],arr2[index])
                if i==n and dp[i][j]!=maxval:
                    return j
        return -1