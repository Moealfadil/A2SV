class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        p1,p2,p3 = 0,1,2
        n = len(nums)
        nums.sort() #[-4,-1,1,2] target 1
        ans = [float("inf"),0] # [2,-1]
        for i in range(n):# 0 , 1 , 2 , 3 
            l=i+1 #3
            r=n-1 #3
            while r>l:
                sm = nums[i] + nums[l] + nums[r] # 2
                df = target - sm 
                df = df if df>=0 else df*-1
                ans = [df,sm] if df <= ans[0] else ans #ans [-1,2]

                if target >= sm: #too low
                    l+=1 
                else: #too high
                    r-=1
        return ans[1]

