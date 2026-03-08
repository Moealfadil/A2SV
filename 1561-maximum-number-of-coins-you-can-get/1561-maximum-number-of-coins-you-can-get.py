class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        count=0
        for i in range(int(len(piles)*(2/3))):
            if i%2==1:
                count+=piles[i]
        return count