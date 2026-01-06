'''
https://leetcode.com/problems/minimum-number-of-coins-for-fruits?envType=problem-list-v2&envId=dynamic-programming
'''

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*(n + 1)
        for i in range(n-1,-1,-1):
            max_reach = 2 * i +1
            if max_reach >= n:
                dp[i] = prices[i]
            else:
                min_future = float("inf")
                for j in range(i + 1,max_reach + 2):
                    min_future = min(min_future, dp[j])
                dp[i] = min_future + prices[i]
        return dp[0]