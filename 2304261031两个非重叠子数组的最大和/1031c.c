int max(int a,int b){
    return a>b? a:b;
}
int slave(int* nums, int numsSize, int firstLen, int secondLen){
    int sum1=0,sum2=0;
    for(int i=0;i<firstLen;++i){
        sum1+=nums[i];
    }
    for (int i=firstLen;i<firstLen+secondLen;++i){
        sum2+=nums[i];
    }
    int res=sum1+sum2;
    int max1=sum1;
    for (int i=0;i<numsSize-firstLen-secondLen;++i){
        sum2=sum2-nums[firstLen+i]+nums[secondLen+firstLen+i];
        sum1=sum1-nums[i]+nums[firstLen+i];
        max1=max(sum1,max1);
        res=max(res,max1+sum2);
    }
    return res;
}
int maxSumTwoNoOverlap(int* nums, int numsSize, int firstLen, int secondLen){
    return max(slave(nums,numsSize,firstLen,secondLen),slave(nums,numsSize,secondLen,firstLen));
}
