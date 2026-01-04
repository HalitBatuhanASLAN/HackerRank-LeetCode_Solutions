'''
https://leetcode.com/problems/coin-change?envType=problem-list-v2&envId=dynamic-programming
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [99999999999999]*(amount+1)
        if(amount <= 0):
            return 0
        dp[0] = 0
        for i in range(1,amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i],dp[i-c] + 1)
        if dp[amount] == 99999999999999:
            return -1
        return dp[amount]