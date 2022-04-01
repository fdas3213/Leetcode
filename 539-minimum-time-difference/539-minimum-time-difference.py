class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutesOfDay = 1440
        
        normalizedTime = []
        #convert time to absolute minute of the day
        for time in timePoints:
            hr, minute = time.split(":")
            total = 0
            if hr!='00':
                total += int(hr)*60
            if minute!='00':
                total += int(minute)
            
            normalizedTime.append(total)
        #sort the time so that the minimum value must be two adjacent values
        normalizedTime.sort()
        
        return min((y-x)%minutesOfDay for x,y in zip(normalizedTime,
                                                    normalizedTime[1:]+normalizedTime[:1]))