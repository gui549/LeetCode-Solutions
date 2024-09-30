class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_angle = 6 * minutes
        hour_angle = 30 * (hour % 12) + 0.5 * minutes
        
        return min(abs(minutes_angle - hour_angle), 360 - abs(minutes_angle - hour_angle))