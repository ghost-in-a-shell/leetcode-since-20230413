int numberOfArithmeticSlices(int* nums, int numsSize){
    if (numsSize<3)  return 0;
    int res=0;
    int diff=nums[1]-nums[0];
    int last=nums[1];
    int l=2;
    for(int i=0;i<numsSize-2;++i){
        int num=nums[i+2];
        int newdiff=num-last;
        if (newdiff==diff) l++;
        else{
            res+=(l-1)*(l-2)/2;
            l=2;
            diff=newdiff;
        }
        last=num;
    }         
    return res+(l-1)*(l-2)/2;
}