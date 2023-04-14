class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        res=0
        diff=nums[1]-nums[0]
        last=nums[1]
        l=2
        for num in nums[2:]:
            newdiff=num-last 
            if newdiff==diff:
                l+=1
            else:
                res+=(l-1)*(l-2)/2
                l=2
                diff=newdiff
            last=num         
        return int(res+(l-1)*(l-2)/2)