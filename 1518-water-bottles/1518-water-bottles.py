class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        max_num=0
        remaining_bottles=numBottles
        while remaining_bottles>=numExchange:
            max_num += numBottles
            numBottles=remaining_bottles//numExchange
            remaining_bottles= remaining_bottles%numExchange + numBottles
        max_num += numBottles
        return max_num
        