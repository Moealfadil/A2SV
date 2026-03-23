class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min_op=float("inf")
        blocks_count={"W":0,"B":0}
        for i in range(k):
            blocks_count[blocks[i]]+=1
        min_op=min(blocks_count["W"],min_op)
        for i in range(k,len(blocks)):
            blocks_count[blocks[i]]+=1
            blocks_count[blocks[i-k]]-=1
            min_op=min(blocks_count["W"],min_op)
        return min_op


