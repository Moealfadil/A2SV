class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        n=len(fruits)
        i=0
        j=0
        taken={}
        count=0
        max_count=0
        while j<n:
            taken[fruits[j]] = taken.get(fruits[j], 0) + 1
            if len(taken)<=2:
                count+=1
            else:
                while len(taken)>2:
                    taken[fruits[i]] -= 1
                    if taken[fruits[i]] == 0:
                        del taken[fruits[i]]
                    count-=1
                    i+=1
                count+=1
            max_count=max(count,max_count)
            j+=1
        return max_count
        