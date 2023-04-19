class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp=[0]*(len(arr)+1)
        for i in range(len(arr)):
            j=i
            maxv=arr[i]
            while j>=0 and j>=i+1-k:
                dp[i+1]=max(dp[i+1],dp[j]+(i+1-j)*maxv)
                if j>0:
                    maxv=max(maxv,arr[j-1])
                j-=1
        return dp[len(arr)]