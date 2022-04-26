class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutesOfDay =1440
        
        def getTime(time):
            hr, minute = time.split(":")
            total = 0
            if hr!='00':
                total += int(hr)*60
            if minute !='00':
                total += int(minute)
            return total
        
        normalizedTime = [getTime(time) for time in timePoints]
        normalizedTime.sort()
        
        
        return min((y-x)%minutesOfDay for x,y in zip(normalizedTime, normalizedTime[1:]+normalizedTime[:1]))