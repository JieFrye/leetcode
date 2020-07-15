# Given two numbers, hour and minutes.
# Return the smaller angle (in degrees) formed between the hour and the minute hand.

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        '''
        ideas:
        360 degrees divided into 6 per min, 30 per hour
        find the minute position of the hour hand
        12:30 = (6-0.5)*30 = 165
        3:30 = (6-3.5)*30 = 75
        3:15 = abs(3.25-3)*30 = 7.5
        4:50 = abs(4+50/60-50/5)*30 = 155
        12:00 = abs(12%12 + 0/60 - 0/5)*30 = 0

        12:45 = 112.5
        '''
        return min(abs(hour % 12 + minutes / 60 - minutes / 5)*30, \
                360 - abs(hour % 12 + minutes / 60 - minutes / 5)*30)

h = 12
m = 46
sol = Solution()
print(sol.angleClock(h,m))
