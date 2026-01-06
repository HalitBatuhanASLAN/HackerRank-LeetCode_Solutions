'''
https://leetcode.com/problems/coin-change-ii?envType=problem-list-v2&envId=dynamic-programming
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if len(coins) == 0: return 0
        if len(coins) == 1 and amount % coins[0] == 0: return 1
        if len(coins) == 1 and amount % coins[0] != 0: return 0
        if amount < 0: return 0
        dp = [0]*(amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin,amount + 1):
                dp[i] += dp[i-coin]
        return dp[amount]
