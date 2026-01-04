'''
https://leetcode.com/problems/min-cost-climbing-stairs?envType=problem-list-v2&envId=dynamic-programming
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if(n < 2):
            return 0
        dp = [0]*(n)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n ):
            if(dp[i-1] > dp[i-2]):
                dp[i] = cost[i] + dp[i-2]
            else:
                dp[i] = cost[i] + dp[i-1]
        if(dp[n-1] > dp[n-2]):
            return dp[n-2] # think like it takes 2 steps without using last stair
        return dp[n-1]