class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low=0
        high=len(letters)-1
        while low<=high:
            mid=(low+high)//2
            if ((mid==0) and letters[mid]>target) or (mid>0 and letters[mid]>target and letters[mid-1]<=target):
                return letters[mid]
            elif letters[mid]<=target:
                low=mid+1
            else:
                high=mid-1
        return letters[0]

