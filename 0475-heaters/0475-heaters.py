class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        i=0
        j=0
        max_r=0
        r=0
        houses.sort()
        heaters.sort()
        if len(heaters)==1:
            return max(abs(heaters[0]-houses[0]), abs(heaters[0]-houses[-1]))
        while i<len(houses) and j<len(heaters)-1:
            while i<len(houses) and abs(heaters[j]-houses[i])< abs(heaters[j+1]-houses[i]):
                r=abs(heaters[j]-houses[i])
                max_r=max(r,max_r)
                i+=1
            j+=1
       
        return max(max_r, houses[-1]-heaters[j])
        

