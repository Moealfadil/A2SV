class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i=0
        j=len(nums)-1
        i_sum=0
        j_sum=0
        final=float('inf')
        while i+1<j:
            i_sum=(nums[i]+nums[i+1]+nums[j])
            j_sum=(nums[i]+nums[j-1]+nums[j])
            if abs(target-i_sum)<abs(target-j_sum):
                if abs(target-i_sum)<abs(target-final):
                    final=i_sum
                else:
                    break
                if abs(target-i_sum)==0:
                    return i_sum
                elif i_sum<target:
                    i+=1
                else:
                    j-=1
            else:
                if abs(target-j_sum)<abs(target-final):
                    final=j_sum
                else:
                    break
                if abs(target-j_sum)==0:
                    return j_sum
                elif j_sum<target:
                   i+=1
                else:
                    j-=1
        return final
            


print(Solution().threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))