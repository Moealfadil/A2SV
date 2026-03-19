class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        check=sum(skill)/(len(skill)/2)
        chemistry=0
        while i<j:
            if skill[i]+skill[j]==check:
                chemistry+=skill[i]*skill[j]
            else:
                return -1
            i+=1
            j-=1
        return chemistry

