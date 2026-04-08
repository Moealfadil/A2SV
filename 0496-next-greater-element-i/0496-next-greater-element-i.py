class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        answer=[]
        n=len(nums2)
        for i in nums1:
            flag=False
            j=nums2.index(i)
            for num in nums2[j:n]:
                if num>i and flag==False:
                    answer.append(num)
                    flag=True
                    break
                elif num==nums2[-1]:
                    answer.append(-1)
        # for i in range(len(answer)):
        #     if answer[i]==0:
        #         answer[i]=-1
        return answer
        