class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        n=len(people)
        people.sort()
        i=0
        j=n-1
        count=0
        total=0
        while i<j:
            if people[i]+people[j]<= limit:
                i+=1
                total+=1
            j-=1
            count+=1
            total+=1
        if total==n:
            return count
        else:
            return count+1
                

