class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        arr,lve=max(arriveAlice,arriveBob),min(leaveAlice,leaveBob)
        return 0 if lve<arr else sum(days[int(arr[:2])-1:int(lve[:2])-1])+int(lve[-2:])-int(arr[-2:])+1
