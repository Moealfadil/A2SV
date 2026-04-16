class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        count = 0
        prev_time = 0

        for pos, s in cars:
            time = (target - pos)/ s

            if time > prev_time:
                count += 1
                prev_time = time
        return count