def isCovered(self, ranges, left, right):
    """
    :type ranges: List[List[int]]
    :type left: int
    :type right: int
    :rtype: bool
    """
    list1=list(range(left,right+1))
    for j in ranges:
        for i in list1:
            if i<=j[1] and i>=j[0]:
                list1.remove(i)
    if list1:
        return False
    else:
        return True
    
print(isCovered(0,[[1,2],[3,4],[5,6]],2,5))