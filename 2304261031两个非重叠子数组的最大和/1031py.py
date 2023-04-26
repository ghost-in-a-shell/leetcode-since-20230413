class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        return max(self.slave(nums,firstLen,secondLen),self.slave(nums,secondLen,firstLen))
    def slave(self,nums: List[int], firstLen: int, secondLen: int):
        sum1=sum(nums[:firstLen])
        sum2=sum(nums[firstLen:firstLen+secondLen])
        res=sum1+sum2
        max1=sum1
        for i in range(len(nums)-firstLen-secondLen):
            sum2=sum2-nums[firstLen+i]+nums[firstLen+secondLen+i]
            sum1=sum1-nums[i]+nums[firstLen+i]
            max1=max(max1,sum1)
            res=max(res,max1+sum2)
        return res
