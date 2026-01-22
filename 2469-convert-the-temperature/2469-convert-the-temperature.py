class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        K= float(celsius) + 273.15
        F=float(celsius) *1.80 + 32.00
        return [K,F]

        