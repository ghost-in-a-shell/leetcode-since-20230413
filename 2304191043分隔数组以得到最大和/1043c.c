int maxSumAfterPartitioning(int* arr, int arrSize, int k){
    int* dp=(int *)malloc((arrSize+1)*sizeof(int));
    memset(dp, 0, sizeof(dp));
    for (int i=0;i<arrSize;++i){
        int j=i;
        int maxval=arr[i];
        while(j>=0 && j>=i+1-k){
            int newval=dp[j]+maxval*(i+1-j);
            dp[i+1]=dp[i+1]>newval? dp[i+1]:newval;
            if (j>0){
                maxval=maxval>arr[j-1]? maxval:arr[j-1];
            }
            --j;
        }
    }
    return dp[arrSize];
}