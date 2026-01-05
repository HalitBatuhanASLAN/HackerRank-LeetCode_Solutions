'''
https://leetcode.com/problems/map-of-highest-peak
'''

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        dp = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    dp[i][j] = 0
        for i in range(m):
            for j in range(n):
                if(dp[i][j] != 0):
                    if i > 0:
                        dp[i][j] = min(dp[i][j],dp[i-1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j],dp[i][j-1] + 1)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if(dp[i][j] != 0):
                    if i < m-1:
                        dp[i][j] = min(dp[i][j],dp[i+1][j] + 1)
                    if j < n-1:
                        dp[i][j] = min(dp[i][j],dp[i][j+1] + 1)
        return dp